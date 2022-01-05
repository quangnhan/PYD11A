from django.contrib import admin
from .models import Customer, Car, Phone, Room

# Register your models here.

admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Phone)
admin.site.register(Room)