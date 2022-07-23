from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Cart
        exclude = ['product']
        # fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    
    category = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Category
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    
    owner = serializers.StringRelatedField(read_only=True)
    review = ProductSerializer(read_only=True)
    class Meta:
        model = models.Review
        # exclude = ['product']
        fields = "__all__"
