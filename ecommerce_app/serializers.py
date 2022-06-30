from rest_framework import serializers
from .models import Product, Category, Review

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        exclude = ['owner']


class CategorySerializer(serializers.ModelSerializer):
    
    category = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Review
        fields = "__all__"
