from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
import random
import string
from .sender import send_otp
import uuid
# Create your models here.


class User(AbstractUser):
    phonenumber = models.CharField(max_length=11,validators=[RegexValidator(r'09(1[0-9]|3[0-9]|2[0-9])-?[0-9]{3}-?[0-9]{4}')])
    address = models.CharField(max_length=500) 
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['phonenumber' , 'address' , 'city' , 'zip_code']
    
    def __str__(self):
        return str(self.username)


class OtpRequestQuerySet(models.QuerySet):
    def is_valid(self, receiver, request, password):
        return self.filter(
            receiver=receiver,
            request_id=request,
            password=password,

        ).exists()



class OTPManager(models.Manager):

    def get_queryset(self):
        return OtpRequestQuerySet(self.model, self._db)

    def is_valid(self, receiver, request, password):
        return self.get_queryset().is_valid(receiver, request, password)


    def generate(self, data):
        otp = self.model( receiver=data['receiver'] )
        otp.save(using=self._db)
        send_otp(otp)
        return otp

def generate_otp():
    rand = random.SystemRandom()
    digits = rand.choices(string.digits, k=4)
    return  ''.join(digits)


class OTPRequest(models.Model):
    request_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    receiver = models.CharField(max_length=50)
    password = models.CharField(max_length=4, default=generate_otp)

    objects = OTPManager()

    
