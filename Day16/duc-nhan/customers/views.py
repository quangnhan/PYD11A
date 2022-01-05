from django.shortcuts import render
from .models import Customer

# Create your views here.
def customerList(request):
    listCustomers = Customer.objects.all()
    data = {
        "customers": listCustomers
    }
    return render(request, "customers/customer_list.html", data)