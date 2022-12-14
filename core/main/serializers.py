from product.models import Product , Category
from rest_framework import serializers
from .models import Banner , Adver

class MainProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = [
            'name',
            'category',
            'image',
            'price',
            'special',
        ]
    


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner

        fields = [
            'Product',
            'pic',
        ]



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

        fields = [
            'id',
            'name',
        ]

class AdverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adver

        fields = [
            'pic', 'name' ,
        ]