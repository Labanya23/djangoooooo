from django.contrib import admin
from . models import Product,Customer,Cart

# Register your models here.



class ProductModelAdmin(admin.ModelAdmin):
    list_displayed = ['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']

admin.site.register(Product, ProductModelAdmin)

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']



