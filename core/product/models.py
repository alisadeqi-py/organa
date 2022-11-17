from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها '


class Product(models.Model):
    name = models.CharField(max_length = 250)
    category = models.ForeignKey(Category , null= True ,on_delete = models.SET_NULL)
    image = models.ImageField(upload_to='images')
    Properties = models.TextField()
    M_taking = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=False)
    special = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now=True)
    Update_date = models.DateTimeField(auto_now_add =True)
    price = models.BigIntegerField()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات '

    def __str__(self):
        return self.name

    
