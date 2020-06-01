from django.contrib import admin
from .models import ProductCategory, Product
#  регистрируем в админке
admin.site.register(ProductCategory)
admin.site.register(Product)
