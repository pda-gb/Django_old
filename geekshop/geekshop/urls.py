"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  # динамические ссылки на страницы
import mainapp.views as mainapp
from django.conf import settings  # для работы с медиа
from django.conf.urls.static import static  # для работы с медиа
from django.conf.urls import include  # для работы с include
urlpatterns = [
    path('', mainapp.main, name='main'),
    path('contact/', mainapp.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
    path('products/', include('mainapp.urls', namespace='products'))
]
#  Смысл этого кода — сообщить Django, что нужно папку на диске MEDIA_ROOT
#  сделать доступной по сетевому адресу MEDIA_URL. Только для режима дебага,
#  в готовом проекте будет раздавть веб-сервер
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)