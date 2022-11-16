from django.contrib import admin
from django.urls import include, path
from .views import Banner , ProductSpecial , CategoryList



urlpatterns = [
   path('banner/', Banner.as_view() , name='Banner-list') , 
   path('products/' , ProductSpecial.as_view() , name = 'Product-detail'),
   path('category/' , CategoryList.as_view() , name = 'category-detail')

    
]