from django.urls import path
from .views import customer_list, customer_create

urlpatterns = [
    path('', customer_list),
    path('create', customer_create),
]
