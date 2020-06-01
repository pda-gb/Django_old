from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from .models import Product, ProductCategory


def main(request):
    current_title = "главная"
    products = Product.objects.all()
    page_content = {"title": current_title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', page_content)


def products(request):
    current_title = "продукты"
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    page_content = {"title": current_title, "links_menu": links_menu}
    return render(request, 'mainapp/products.html', page_content)


def contact(request):
    current_title = "контакты"
    page_content = {"title": current_title}
    return render(request, 'mainapp/contact.html', page_content)
