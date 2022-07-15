from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    
    category = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Category
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Review
        fields = "__all__"
        

class CartSerializer(serializers.ModelSerializer):
    carts = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Cart
        fields = "__all__"