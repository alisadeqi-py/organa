from django.contrib import admin
from django.urls import include, path
from .views import CartView , exists


urlpatterns =[
   path('', CartView.as_view() , name='Product-list'),
   path('exists/', exists.as_view() , name='exists') 
   
]