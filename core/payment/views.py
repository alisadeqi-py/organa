from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json
from cart.models import Cart
from mail_templated import send_mail
from rest_framework import generics
from rest_framework.response import Response
from core import settings

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
description = "خرید از وبسایت استاد مهدی علی نجفی"  # Required
""" email = 'email@example.com'  # Optional
mobile = '09123456789' """  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/verify/'


def send_request(request , price , cart_id):
    global amount
    global cart
    cart = cart_id
    amount = price 
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                cart = Cart.objects.get(id = cart)
                cart.order = True 
                cart.save()
                return HttpResponse('Transaction success')
            elif t_status == 101:
                return HttpResponse('Transaction submitted')
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')


class TestEmail(generics.GenericAPIView):

    def get(self , request , *args, **kwargs):
        

        send_mail('email/emailtemp.tpl', {'name': 'ali'}, 'sadeqiali2000@gamil.com', ['engsadeghi78@gmail.com'])
        
        return Response('email sent')





