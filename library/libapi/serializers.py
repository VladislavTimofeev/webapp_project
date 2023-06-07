from rest_framework import serializers
from .models import User
from django.db import models


# need changes
def get_user_by_id(obj):
    user_id = models.User.objects.filter(user_id=obj.id)
    serializer = UserSerializer(user_id, many=True)
    return serializer.data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
