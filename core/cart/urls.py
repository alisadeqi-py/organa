from django.contrib import admin
from django.urls import include, path
from .views import CartView , exists , Delete


urlpatterns =[
   path('', CartView.as_view() , name='Product-list') ,
   path('<int:id>/', Delete.as_view() , name='delete') ,
   path('exists/<int:id>/', exists.as_view() , name='exists')

]