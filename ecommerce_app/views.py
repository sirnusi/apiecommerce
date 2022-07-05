from django.shortcuts import render
from rest_framework import generics, filters
from . import models, serializers, pagination, permissions

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductListAV(ListAPIView):
    
    serializer_class = serializers.ProductSerializer
    pagination_class = pagination.ProductListPagination
    
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['category__name', 'price']
    search_fields = ['name']
    ordering_fields = ['price']
    
    
    def get_queryset(self):
        owner = self.request.user
        return models.Product.objects.filter(owner=owner)

class ProductCreateAV(CreateAPIView):
    serializer_class = serializers.ProductSerializer
    
    def get_queryset(self):
        return models.Product.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
   
class ProductDetailAV(RetrieveUpdateDestroyAPIView):
    
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.ProductOwnerOrReadOnly]
    
    def get_queryset(self):
        return models.Product.objects.all()

    def perform_update(self, serializer):
        pk = self.kwargs.get('pk')
        product = models.Product.objects.get(pk=pk)
        
        if product.quantity == 1:
            return product.price
        else:
            product.price += product.price
            return product.price
        pass
        

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

class ReviewDetailAV(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOnlyAdminUser]