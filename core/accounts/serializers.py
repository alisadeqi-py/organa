from rest_framework import serializers 
from .models import User , OTPRequest
from django.core import exceptions
from  django.contrib.auth.password_validation import validate_password
from cart.models import Cart
class RegistrationSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(max_length=12 , write_only=True)

    class Meta:
        model = User 
        fields = [  'first_name','last_name', 'phonenumber' , 'email' , 'password' , 'password1' , 'address' , 'username'] 



    def validate(self ,attr ):
        if attr.get('password') != attr.get('password1'):
            raise serializers.ValidationError({'datail': 'passwords doesnot match'})
        try:
            validate_password(attr.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages) })
        return super().validate(attr)
        
"""     def create(self , validated_data):
        
        validated_data.pop('password1', None)
        
        return User.objects.create_user(validated_data) """


class UserUpdateSerializer(serializers.ModelSerializer):


    class Meta:
        model = User 
        fields = [  'first_name','last_name', 'phonenumber' , 'email' , 'address' , 'username'] 

class ChangePasswordSerialier(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError({"detail": "passswords doesnt match"})

        try:
            validate_password(attrs.get("new_password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})

        return super().validate(attrs)


class CartSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cart

        fields = '__all__'


class RequestOTPSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=50, allow_null=False)

class RequestOTPResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPRequest
        fields =['request_id']

class VerifyOtpRequestSerializer(serializers.Serializer):
    request_id = serializers.UUIDField(allow_null=False)
    password = serializers.CharField(max_length=4, allow_null=False)
    receiver = serializers.CharField(max_length=64, allow_null=False)