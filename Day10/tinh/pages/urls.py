from django.urls import path
from .views import *

urlpatterns = [
    path('users', users),
    path('user_list', user_list),
    path('products', product_list),
]
