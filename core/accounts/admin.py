from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets += (
    ('phone_number' , {'fields':('phonenumber',)}) ,
    ('address' , {'fields':('address',)}) , 
    ('city' , {'fields':('city',)}) ,
    ('zip_code' , {'fields':('zip_code',)}),
    ('state' , {'fields':('state',)}))

admin.site.register(User, UserAdmin)

