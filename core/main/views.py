from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from product.models import Product , Category
from .models import Banner , Adver
from .serializers import MainProductSerializer , BannerSerializer , CategorySerializer , AdverSerializer




class Banner(ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()

class ProductSpecial(ListAPIView):
    serializer_class = MainProductSerializer
    queryset = Product.objects.filter(status = True , special = True)


class CategoryList(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class Adver(ListAPIView):
    serializer_class = AdverSerializer
    queryset = Adver.objects.all()