from blog.models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
   
    class Meta:
        model = Category
        fields = ['cat_name', 'posts']