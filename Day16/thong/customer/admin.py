from django.contrib import admin
from .models import Customer, Car, Book, Room

# Register your models here.
admin.site.register(Customer)

admin.site.register(Car)
admin.site.register(Book)
admin.site.register(Room)