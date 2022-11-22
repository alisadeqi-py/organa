from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True, source="category.name")

    class Meta:
        model = Product

        fields = [
            'id',
            'name',
            'category_name',
            'image',
            'Properties',
            'M_taking',
            'description',
            'price',
            'status'
        ]