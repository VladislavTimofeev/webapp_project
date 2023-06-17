from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import *


class AuthorDetailApiView(APIView):

    # 5. Delete
    def delete(self, request, author_id, *args, **kwargs):

        # Deletes the author with given author_id if exists

        author = Author.objects.filter(id=author_id)

        if not author:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        author.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

    # 4. Update
    def put(self, request, author_id, *args, **kwargs):

        # Updates the author with given author_id if exists

        author = Author.objects.filter(id=author_id).first()

        if not author:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name')
        }
        serializer = AuthorSerializer(author, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    # 3. Retrieve author by author_id
    def get(self, request, author_id, *args, **kwargs):

        # Retrieves the Author with given author_id

        author = Author.objects.filter(id=author_id)

        if author:
            serializer = AuthorSerializer(author, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )


class AuthorListApiView(APIView):

    # 1. Get authors
    def get(self, request, *args, **kwargs):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Add authors
    def post(self, request, *args, **kwargs):
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name')
        }
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailApiView(APIView):

    # 5. Delete
    def delete(self, request, book_id, *args, **kwargs):

        # Deletes the book with given book_id if exists

        book = Book.objects.filter(id=book_id)

        if not book:
            return Response(
                {"res": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        book.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

    # 4. Update
    def put(self, request, book_id, *args, **kwargs):

        # Updates the book with given book_id if exists

        book = Book.objects.filter(id=book_id).first()

        if not book:
            return Response(
                {"res": "Object with book id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title')
        }
        serializer = BookSerializer(book, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    # 3. Retrieve book by book_id
    def get(self, request, book_id, *args, **kwargs):

        # Retrieves the Book with given book_id

        book = Book.objects.filter(id=book_id)

        if book:
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"res": "Object with book id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )


class BookListApiView(APIView):

    # 1. Get books
    def get(self, request, *args, **kwargs):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Add books
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'author': request.data.get('author')
        }
        print(request.data.get('author'))
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
