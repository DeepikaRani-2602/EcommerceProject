from django.contrib import admin

from app.models import Product, Checkout

# Register your models here.


class EcommerceAdmin(admin.ModelAdmin):
    list_display = ['name']

    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product, EcommerceAdmin)
admin.site.register(Checkout)
