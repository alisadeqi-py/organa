from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView
from .serializers import ProductSerializer
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend

class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(status = True , )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','category','price']


class ProductDetail(RetrieveAPIView):
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

