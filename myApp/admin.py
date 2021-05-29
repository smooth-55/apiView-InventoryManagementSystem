from django.contrib import admin
from .models import Product, Sku, Batch, Inventory

# Register your models here.

admin.site.register(Product)
admin.site.register(Sku)
admin.site.register(Batch)
admin.site.register(Inventory)
