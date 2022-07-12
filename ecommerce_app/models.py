from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                related_name='category')
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.rating) | self.product.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.name

# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL)
#     address = models.CharField(max_length=250, null=False)
#     city = models.CharField(max_length=300, null=False)
#     state = models.CharField(max_length=100, null=False)
#     zipcode = models.CharField(max_length=50, null=False)
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.address