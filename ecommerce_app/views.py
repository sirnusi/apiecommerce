from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView, ListAPIView, 
                                     CreateAPIView, RetrieveUpdateDestroyAPIView)
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from .permissions import ProductOwnerOrReadOnly, IsOnlyAdminUser
from .pagination import ProductListPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductListAV(ListAPIView):
    #queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductListPagination
    #permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['category__name', 'price']
    search_fields = ['name']
    #ordering_fields = ['price']
    
    
    def get_queryset(self):
        owner = self.request.user
        return Product.objects.filter(owner=owner)

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


class ReviewListAV(ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(product=pk)

class ReviewCreateAV(CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        product = Product.objects.filter(pk=pk)
        
        return Review.objects.filter(product=product)
        