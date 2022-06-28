from django.db import models
from django.contrib.auth.models import User

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
    price = models.FloatField()
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name