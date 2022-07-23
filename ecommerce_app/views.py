from django.shortcuts import render
from rest_framework import generics, filters, views, response, status, parsers
from rest_framework.serializers import ValidationError
from . import models, serializers, pagination, permissions

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductListAV(generics.ListAPIView):
    
    serializer_class = serializers.ProductSerializer
    pagination_class = pagination.ProductListPagination
    
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['category__name', 'price']
    search_fields = ['name']
    ordering_fields = ['price']
    
    
    def get_queryset(self):
        owner = self.request.user
        if owner.is_authenticated == False:
            raise ValidationError({'error':'Go login'})
        return models.Product.objects.filter(owner=owner)

class ProductCreateAV(generics.CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.ProductOwnerOrReadOnly]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
     
    def perform_create(self, serializer):
        owner = self.request.user
        if owner.is_authenticated != owner:
            raise ValidationError({'Error':
                'You are trying to create product using another user'})
        serializer.save(owner=owner)     
    
class ProductDetailAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.ProductOwnerOrReadOnly]
    
    def get_queryset(self):
        try:
            pk= self.kwargs.get('pk')
            product = models.Product.objects.get(pk=pk)
        
        except models.Product.DoesNotExist:
            raise ValidationError('Error: No product with the pk {pk}'.format(pk=pk))
        
        
class CategoryListAV(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    

class CategoryCreateAV(generics.CreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsOnlyAdminUser]


class CategoryDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsOnlyAdminUser]


class ReviewListAV(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.Review.objects.filter(product=pk)

class ReviewCreateAV(generics.CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    
    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        owner = self.request.user
        product = models.Product.objects.filter(pk=pk)
        
        review_set = models.Review.objects.filter(product=product, owner=owner)
        
        if review_set.exists():
            raise serializers.ValidationError({'Error': 'You have rated this product'})
        
        serializer.save(owner=owner, product=product)

class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsOnlyAdminUser]


class CartListAV(generics.ListAPIView):
    serializer_class = serializers.CartSerializer
    
    def get_queryset(self):
        owner = self.request.user
        return models.Cart.objects.filter(owner=owner)


class CartCreateAV(generics.CreateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer
    permission_classes = [permissions.IsAuthenticated]


class CartDetailAV(generics.DestroyAPIView):
    serializer_class = serializers.CartSerializer
    permission_classes = [permissions.IsCartOwnerOnly]
    
    def get_queryset(self):
        pk= self.kwargs.get('pk')
        return models.Product.objects.filter(pk=pk)
    
        