from django.shortcuts import  render 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart , CartItems
from product.models import Product
from .serializers import * 


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.filter(user = user.id , order = False).first()
        queryset = CartItems.objects.filter(cart = cart)
        serializer  = CartItemSerializers(queryset ,  many = True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        cart , created = Cart.objects.get_or_create(user=user , order = False)
        product = Product.objects.get(id = data['product'])
        price = product.price
        quantity = data.get('quantity')
        cart_Item , created = CartItems.objects.get_or_create( cart = cart , user = user , product = product , price = price  , quantity = quantity)
        cart_Item.save()
        return Response('good job')
   
    def put(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        product = Product.objects.get(id = data['product'])
        cart = Cart.objects.filter(user = user.id , order = False).first()
        cart_item = CartItems.objects.get( cart = cart ,  user = user , product = product )
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response('item updated')
  
    def delete(self, request, *args, **kwargs): 
        user = request.user
        data = request.data
        cart = Cart.objects.filter(user = user.id , order = False).first()
        product = Product.objects.get(id = data['product'])
        cart_item = CartItems.objects.get( cart = cart , user = user , product = product)
        cart_item.delete()
        return Response('deleted')