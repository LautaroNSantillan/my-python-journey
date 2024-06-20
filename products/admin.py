from django.contrib import admin
from .models import Product, Discount


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Discount, DiscountAdmin)
admin.site.register(Product, ProductAdmin)


