from django.contrib import admin

from .models import Product, Contactenquiry


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cat', 'details', 'is_active']
    list_filter = ['cat', 'is_active']


admin.site.register(Product, ProductAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


admin.site.register(Contactenquiry, ContactAdmin)