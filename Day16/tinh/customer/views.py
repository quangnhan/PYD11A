from django.shortcuts import render
from .models import Customer

# Create your views here.
def customerList(request):
    list_customers = Customer.objects.all()
    data = {
        "list_customers": list_customers
    }
    
    return render(request, "customer/customer_list.html", data)