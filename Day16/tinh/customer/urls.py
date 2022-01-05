from django.urls import path
from .views import customerList

urlpatterns = [
    path('', customerList)
]