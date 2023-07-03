from .models import Product, Category
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image']

class related(serializers.RelatedField):
    def to_representation(self, value):
        return {"name": value.name, "description": value.description, "category": value.category.name, "image": value.image.url}

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
