from django.shortcuts import render


# Create your views here.
def main(request):
    current_title = "главная"
    products = [
        {
            "name": "отличный стул",
            "desc": "вам понравится",
            "image_src": "product-1.jpg",
            "image_href": "/product/1/",
            "alt": "продукт 1"
        },
        {
            "name": "стул !!!!!",
            "desc": "что надо!!",
            "image_src": "product-2.jpg",
            "image_href": "/product/2/",
            "alt": "продукт 2"
        }
    ]
    page_content = {"title": current_title, "products": products}
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
