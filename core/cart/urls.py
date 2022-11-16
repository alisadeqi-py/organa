from django.contrib import admin
from django.urls import include, path
from .views import CartView


urlpatterns =[
   path('', CartView.as_view() , name='Product-list') , 
   
]