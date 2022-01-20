from rest_framework import serializers
from articles.models import Category, Articles


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'category',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            'title',
            'description',
            'article',
            'category',
            'publish',
            'author',
        )
