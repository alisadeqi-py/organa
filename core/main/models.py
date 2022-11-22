from django.db import models

# Create your models here.


from django.db import models
from product.models import Product
# Create your models here.


class Banner(models.Model):
    Product = models.ForeignKey(Product , on_delete = models.CASCADE)
    pic = models.ImageField(upload_to='images/banner')


class Adver(models.Model):
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='images/adver')

    class Meta:
        verbose_name = 'تبلیغ'
        verbose_name_plural= "تبلیغات"



