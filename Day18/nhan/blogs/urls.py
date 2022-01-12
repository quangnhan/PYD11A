from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_list"),
    path('create', BlogCreateView.as_view(), name="blog_create"),
]
