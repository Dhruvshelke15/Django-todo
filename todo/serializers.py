# todo/serializers.py
from rest_framework import serializers
from .models import TodoItem, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = TodoItem
        fields = '__all__'
