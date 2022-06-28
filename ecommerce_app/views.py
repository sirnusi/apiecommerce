from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView, ListAPIView, 
                                     CreateAPIView, RetrieveUpdateDestroyAPIView)
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .permissions import ProductOwnerOrReadOnly, IsOnlyAdminUser
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductListAV(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductCreateAV(CreateAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
   
class ProductDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductOwnerOrReadOnly]
    # only the people that created that can delete it but anybody can read it.


class CategoryListAV(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class CategoryCreateAV(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOnlyAdminUser]


class CategoryDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsOnlyAdminUser]


