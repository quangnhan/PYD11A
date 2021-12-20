from django.urls import path
from .views import *

urlpatterns = [
<<<<<<< HEAD
    path("users", users),
    path("user_list", product_list),
=======
    path('users', users),
    path('user_list', user_list),
    path('products', product_list),
>>>>>>> dd5b8ab8e2e992460d59d4c755158c03b2701d13
]
