from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Product
        exclude = ['owner']


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