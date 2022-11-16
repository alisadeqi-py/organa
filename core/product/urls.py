from django.contrib import admin
from django.urls import include, path


from django.contrib import admin
from django.urls import include, path

from .views import ProductList , ProductDetail



urlpatterns = [
    path('list/', ProductList.as_view() , name='Product-list') , 
    path('<pk>/' , ProductDetail.as_view() , name = 'Product-detail')
    
]