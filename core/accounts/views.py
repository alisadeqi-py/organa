from urllib import response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import  ( RegistrationSerializer , UserUpdateSerializer , ChangePasswordSerialier ,
                             CartSerializers , RequestOTPSerializer , RequestOTPResponseSerializer ,
                             VerifyOtpRequestSerializer , UserNameSerializer)
from .models import User , OTPRequest
from cart.models import Cart
from django.shortcuts import get_object_or_404



class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            User.objects.create_user(username = serializer.data['username'] ,
            email = serializer.data['email'] , address = serializer.data['address'] , password = serializer.data['password']
             , first_name = serializer.data['first_name'] , last_name = serializer.data['last_name'] , phonenumber = serializer.data['phonenumber'] , zip_code = serializer.data['zip_code'],
              city = serializer.data['city'] , state = serializer.data['state'])
            serializer.save
            data = {
                    'first_name':serializer.validated_data['first_name']
                }
            return Response(data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors , status.HTTP_400_BAD_REQUEST)



class UserUpdateApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id = request.user.id)
        serializer = UserUpdateSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user_r = request.user
        data = request.data
        user = User.objects.get(id = user_r.id)
        user.username = data.get('username')
        user.email = data.get('email')
        user.address = data.get('address')
        user.phonenumber = data.get('phonenumber')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.zip_code = data.get('zip_code')
        user.state = data.get('state')
        user.city = data.get('city')
        user.save()
        return Response('user updated')


class ChangePasswordApiView(generics.GenericAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerialier

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"details": "password changed successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self , request):
        request.user.auth_token.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class CartView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializers
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class OTPView(APIView):
    def get(self, request):
        serializer = RequestOTPSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                otp = OTPRequest.objects.generate(data)
                return Response(data= RequestOTPResponseSerializer(otp).data)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)


    def post(self, request):
        serializer = VerifyOtpRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if OTPRequest.objects.is_valid(data['receiver'], data['request_id'], data['password']):
                return Response('pass correct')
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)

class BasketFinal(APIView):
    def get(self, request):
        user = User.objects.get(id = request.user.id)
        serializer = UserNameSerializer(user)
        return Response(serializer.data)
    
