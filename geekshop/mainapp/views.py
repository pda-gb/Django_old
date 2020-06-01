from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from .models import Product, ProductCategory


def main(request):
    current_title = "главная"
    products = Product.objects.all()
    page_content = {"title": current_title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', page_content)


def products(request, pk=None):
    current_title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_product = Product.objects.all()
    page_content = {
                    "title": current_title,
                    "links_menu": links_menu,
                    "same_product": same_product,
                    "media_url": settings.MEDIA_URL
                    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, 'mainapp/products.html', page_content)


def contact(request):
    current_title = "контакты"
    page_content = {"title": current_title}
    return render(request, 'mainapp/contact.html', page_content)
