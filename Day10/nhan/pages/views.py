import json
from database import Database
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

def users(request):
    tuple_user = Database().get_all_user()
    list_user = []
    for user in tuple_user:
        list_user.append({
            "id": user[0],
            "name": user[1],
        })
    return JsonResponse(list_user, safe=False)

def user_list(request):
    tuple_user = Database().get_all_user()
    list_user = []
    for user in tuple_user:
        list_user.append({
            "id": user[0],
            "name": user[1],
        })
    data = {
        "list_user":list_user
    }
    return render(request, "user_list.html", data)

def product_list(request):
    tuple_product = Database().get_all_product()
    list_product = []
    for product in tuple_product:
        list_product.append({
            "id": product[0],
            "category_id": product[1],
            "category_name": product[2],
            "name": product[3],
        })
    return JsonResponse(list_product, safe=False)