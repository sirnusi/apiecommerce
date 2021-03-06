from django.urls import path
from . import views

urlpatterns = [
    path('products/',  views.ProductListAV.as_view(), name='product-list'),
    path('products/create/', views.ProductCreateAV.as_view(), name='product-create'),
    path('products/<int:pk>/', views.ProductDetailAV.as_view(), name='product-detail'),
    
    path('category/', views.CategoryListAV.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetailAV.as_view(), name='category-detail'),
    path('category/create/', views.CategoryCreateAV.as_view(), name='category-create'),
    
    path('review/<int:pk>/list/', views.ReviewListAV.as_view(), name='review-list'),#review for a product.
    path('review/<int:pk>/create/', views.ReviewCreateAV.as_view(), name='review-create'),
    path('review/<int:pk>/details/', views.ReviewDetailAV.as_view(), name='review-details'),
    
    path('customer/cart/', views.CartListAV.as_view(), name='cart-list'),
    path('customer/<int:pk>/create/', views.CartCreateAV.as_view(), name='cart-create'),
    
    #pk is the product in that cart you want to delete.
    path('customer/cart/<int:pk>/', views.CartDetailAV.as_view(), name='cart-detail'),
    
]