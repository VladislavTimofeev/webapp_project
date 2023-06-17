from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *
import re


def validate_string(pattern, string):
    if re.match(pattern, string):
        return True
    else:
        return False


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']

    def validate(self, data):

        errors = []

        first_name = data['first_name']
        last_name = data['last_name']

        pattern = '^[a-zA-Z]*$'  # Regex pattern: only alphanumeric characters
        print(data['first_name'])
        print(data['last_name'])

        if not validate_string(pattern, first_name):
            errors.append('Wrong your first_name')

        if not validate_string(pattern, last_name):
            errors.append('Wrong your last_name')

        if errors:
            raise ValidationError(errors)

        return data


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author']

    def validate(self, data):
        author_data = data.pop('author')
        book = Book.objects.create(**data)
        # print(data)
        # print(author_data)

        for value in author_data:
            Author.objects.create(book=book, **value)
        return book

        # author = data['authors']
        # for value in range(len(data['authors'])):
        #     print(data['authors'][value]['first_name'])
        #     print(data['authors'][value]['last_name'])
        # return data


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ['id', 'book_id', 'author_id']
