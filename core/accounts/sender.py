""" def send_otp(otp):
    print('otp receiver')
    print(otp.receiver)
    print("otp password")
    print(otp.password)

 """
from kavenegar import *
import json

API_KEY = '6E582B6D4B74636A32343272306136664262696D4D52514B786E726E4C2B6737624658696B3152637553343D'


def send_otp(otp):
    try:
        api = KavenegarAPI(API_KEY)
        reciever = otp.receiver
        token = otp.password
        response = api.verify_lookup( {'receptor': reciever ,'token' : token ,'template': 'organa'})
        print(str(response))
    
    except APIException as e:
        print(str(e))
    except HTTPException as e:
        print(e) 