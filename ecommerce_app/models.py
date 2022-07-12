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
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
   
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

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=0)
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