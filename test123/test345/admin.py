from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(StockIn)
admin.site.register(StockOut)

