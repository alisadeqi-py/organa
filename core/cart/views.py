from django.shortcuts import  render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart , CartItems
from product.models import Product
from .serializers import CartItemSerializers


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.filter(user = user.id , order = False).first()
        queryset = CartItems.objects.filter(cart = cart)
        serializer  = CartItemSerializers(queryset ,  many = True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        product = Product.objects.get(id = data['id'])
        cart , cart_created = Cart.objects.get_or_create(user = user , order = False)
        cart_Item , created = CartItems.objects.get_or_create( cart = cart ,  user = user , product = product )
        quantity = data.get('quantity') 
        cart_Item.quantity = quantity
        cart_Item.price = product.price
        cart_Item.save()
        items = CartItems.objects.filter(user = user)
        total_price = 0
        for item in items:
            total_price += (item.price * item.quantity)
        cart.total_price = total_price

        cart.save()

        return Response('item updated')

class Delete(APIView):
    def delete(self, request,id):
        user = request.user
        cart = Cart.objects.filter(user = user.id , order = False).first()
        product = Product.objects.get(id = id)
        cart_item = CartItems.objects.get( cart = cart , user = user , product = product)
        cart_item.delete()
        product = Product.objects.get(id = id)
        cart , cart_created = Cart.objects.get_or_create(user = user , order = False)
        items = CartItems.objects.filter(user = user)
        total_price = 0
        for item in items:
            total_price += (item.price * item.quantity)
        cart.total_price = total_price
        cart.save()
        return Response('deleted')

class exists(APIView):
    def get(self, request, id):
        user = request.user
        product = Product.objects.get(id =id)
        if CartItems.objects.filter(user = user , product = product ,  isOrder = False).exists() and Cart.objects.filter(user = user , order = False).exists():
            return Response('true')

        return Response('False')