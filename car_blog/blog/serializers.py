from rest_framework import serializers

from .models import Category, Post, Element

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = (
            "id",
            "innerHtml",
            "element_type",
            "image",
            "thumbnail"
        )

class PostSerializer(serializers.ModelSerializer):
    elements = ElementSerializer(many=True)
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "short_desc",
            "elements"
        )

class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "posts"
        )
