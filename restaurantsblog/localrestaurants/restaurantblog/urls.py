"""Restaurants URL Configuration

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
from django.conf.urls import url
from . import views

app_name = 'restaurantblog'

urlpatterns = [
   url(r'^$',views.index, name='index'),
   
    
    url(r'^restaurant$', views.restaurant_list, name='restaurant_list'),

     url(r'^categories$', views.restaurant_category_list, name='restaurant_category_list'),

    url(r'^categories/(?P<category_id>[0-9]+)/$', views.restaurant_category_detail, name='restaurant_category_detail'),
   

    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/$', views.restaurant_detail, name='restaurant_detail'),
    
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/reviews/create/\$', views.review_create, name='review_create'),
]
