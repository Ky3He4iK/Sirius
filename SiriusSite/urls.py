"""SiriusSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

import Site
import Api

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/get', Api.get_school),
    path('api/get/', Api.get_school),
    path('api/adv_search', Api.adv_search),
    path('api/adv_search/', Api.adv_search),
    path('api/search', Api.search),
    path('api/search/', Api.search),
    path('api/lists', Api.get_lists),
    path('api/lists/', Api.get_lists),
    path('', Site.main_page, name="index"),
    path('main', Site.main_page, name="index"),
    path('main/', Site.main_page, name="index"),
    path('humans.txt', Site.humans),
    path('search', Site.adv_search),
    path('search/', Site.adv_search),
    path('school', Site.school),
    path('school/', Site.school),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
