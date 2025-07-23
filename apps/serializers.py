from rest_framework import serializers
from .models import Category, Product, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'quantity', 'price', 'category']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'full_name', 'email', 'phone_number']
        read_only_fields = ['qr_code_image']
