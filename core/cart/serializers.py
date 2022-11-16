from .models import Cart , CartItems
from rest_framework import serializers
from product.serializers import *

class CartSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cart

        fields = '__all__'



class CartItemSerializers(serializers.ModelSerializer):
    cart = CartSerializers()
    product = ProductSerializer()
    class Meta:
        model = CartItems
        fields = ['product' , 'quantity']
