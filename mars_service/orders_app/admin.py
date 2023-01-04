from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order, Device, Customer, DeviceInField

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', "manufacturer", 'model')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_address', 'customer_city')

class DevicesInFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'customer_id', 'analyzer_id', 'owner_status')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'customer_id', 'order_description', 'created_dt', 'last_updated_dt', 'order_status')

admin.site.register(Device, DeviceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DeviceInField, DevicesInFieldAdmin)
admin.site.register(Order, OrderAdmin)