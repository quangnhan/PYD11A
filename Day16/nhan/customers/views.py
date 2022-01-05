from django.shortcuts import render
from .models import Customer

# Create your views here.

def customer_list(request):
    list_customer = Customer.objects.all()
    data = {
        "list_customer" : list_customer
    }
    return render(request, "customers/customer_list.html", data)