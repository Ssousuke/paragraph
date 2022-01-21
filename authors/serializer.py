from rest_framework import serializers
from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'profile',
            'name',
            'user_name',
            'bio',
            'status',
        )
