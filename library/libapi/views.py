from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import User
from .serializers import UserSerializer


class UserDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 5. Delete
    def delete(self, request, user_id, *args, **kwargs):

        # Deletes the user item with given user_id if exists

        user = User.objects.filter(id=user_id)

        if not user:
            return Response(
                {"res": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        user.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

    # 4. Update
    def put(self, request, user_id, *args, **kwargs):

        # Updates the user item with given user_id if exists

        user = User.objects.filter(id=user_id).first()

        if not user:
            return Response(
                {"res": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name')
        }
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    # 3. Retrieve user by user_id
    def get(self, request, user_id, *args, **kwargs):

        # Retrieves the User with given user_id

        user = User.objects.filter(id=user_id)

        if user:
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )


class UserListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. Get users
    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create user
    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
