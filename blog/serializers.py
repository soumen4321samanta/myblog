from rest_framework import serializers
from .models import Posted, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','slug']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['id','name']    

class PostSerializer(serializers.ModelSerializer):
    author   = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    tag      = TagSerializer(many=True, read_only=True)

    class Meta:
        model  = Posted
        fields = [
            'id', 'title', 'body', 'status',
            'created_at', 'author', 'category', 'tag'
        ]