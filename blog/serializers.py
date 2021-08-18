from rest_framework import serializers
  
from .models import Author, Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("image", "about_me")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ("title", "date", "excerpt", "image", "slug")