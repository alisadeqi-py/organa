from django.db import models
from accounts.models import User
from product.models import Product
from django.db.models.signals import pre_save , post_save
from django.dispatch import receiver
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.BooleanField(default=False)
    total_price = models.IntegerField(default= 0 )
    sent = models.BooleanField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.id)
    
    
    def get_price(self):
         
        return self.total_price


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default = 0)
    isOrder = models.BooleanField(default=False)
    quantity = models.IntegerField(default= 1 )

    def __str__(self):

        return str(self.user.username) + " " + str(self.product.name)
    
