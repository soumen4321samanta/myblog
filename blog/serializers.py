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
    author=serializers.StringRelatedField() #author er name show korbe
    category=CategorySerializer() #category er name show korbe
    tag=TagSerializer(many=True) #tag er name show korbe

    class Meta:
        model=Posted
        fields=['id', 'title', 'body', 'status',
            'created_at', 'author', 'category', 'tag']