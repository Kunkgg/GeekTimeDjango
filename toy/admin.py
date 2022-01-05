from django.contrib import admin

# Register your models here.
from .models import Customers
from .models import Orderitems
from .models import Orders
from .models import Productnotes
from .models import Products
from .models import Vendors

admin.site.register(Customers)
admin.site.register(Orderitems)
admin.site.register(Orders)
admin.site.register(Productnotes)
admin.site.register(Products)
admin.site.register(Vendors)
