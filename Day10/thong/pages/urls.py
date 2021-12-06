from django.urls import path
from .views import *

urlpatterns = [
    path("users", users),
    path("user_list", product_list),
]
