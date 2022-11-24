from django.urls import path
from rest_framework.authtoken import views
from .views import (CustomDiscardAuthToken , RegistrationApiView , UserUpdateApiView ,
                     ChangePasswordApiView , CartView , OTPView ,BasketFinal)
urlpatterns = [
    #registration 
    path('registration/' , RegistrationApiView.as_view() , name='registration'),
    path('update/' , UserUpdateApiView.as_view() , name='UserUpdate'),
    path('changepass/' , ChangePasswordApiView.as_view() , name = 'reserpassword'),
    path('carts/' , CartView.as_view() , name = 'Cart'),
    path('BasketFinal/' , BasketFinal.as_view() , name = 'username'),

    # authentication
    path('otp/', OTPView.as_view(), name='otp_view'),

   
    #auth_token 
    path('token/login/' , views.ObtainAuthToken.as_view() , name='auth_token'),
    path('token/logout/' , CustomDiscardAuthToken.as_view() , name='auth_token'),
    ]
# 