from django.contrib import admin
from .models import Cart , CartItems
# Register your models here.




#admin.site.register(Cart , CartAdmin)



class CartItemsInline(admin.TabularInline):
    model = CartItems
    extra = 0



class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemsInline]
    list_display =  (
    'user' ,  'order' ,  'total_price' , 'sent',  
    )
    list_filter = ('sent' , 'order')
    raw_id_fields =  ('user',)






admin.site.register(Cart , CartAdmin)
