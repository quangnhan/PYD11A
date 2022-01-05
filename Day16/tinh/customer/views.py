from django.shortcuts import render

# Create your views here.
def customerList(request):
    return (request, "customer/customer_list.html")