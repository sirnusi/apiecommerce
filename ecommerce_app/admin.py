from django.contrib import admin
from .models import Category, Product, Review

# Register your models here.

admin.site.register((Category, Product, Review))
