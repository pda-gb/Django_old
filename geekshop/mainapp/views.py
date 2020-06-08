from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
# импортируем из моделей классы, для работы с данными из бд
from .models import Product, ProductCategory, Contact


def main(request):
    current_title = "главная"
    products = Product.objects.all()[:4]
    page_content = {"title": current_title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', page_content)


def products(request, pk=None):
    current_title = "продукты"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    page_content = {
                    "title": current_title,
                    "links_menu": links_menu,
                    "same_products": same_products,
                    "media_url": settings.MEDIA_URL
                    }
    if pk:
        print(f"User select category: {pk}")
    return render(request, 'mainapp/products.html', page_content)


def contact(request):
    current_title = "контакты"
    # visit_date = timezone.now() /// "visit_date": visit_date,
    locations = Contact.objects.all()
    page_content = {"title": current_title, "locations": locations}
    return render(request, 'mainapp/contact.html', page_content)
