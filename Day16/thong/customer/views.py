from django.shortcuts import render, HttpResponse
from .models import Customer

# Create your views here.
def customer_list(request):
    list_customer = Customer.objects.all()
    data = {"list_customer": list_customer}
    return render(request, "customers/customer_list.html", data)


def customer_create(request):
    name = request.POST.get("name")
    age = request.POST.get("age")

    Customer.objects.create(name=name, age=age)
    return HttpResponse(True)