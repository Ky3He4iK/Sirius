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

import Site
import Map
import Api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', Map.give_map),
    path('api/get', Api.get_school), # <int: id>
    path('api/search', Api.search),
    # path('', Site.main_page, name="index"),
    path('school/<int: id>', Site.school_info),
] + static("", document_root=settings.MEDIA_ROOT)
