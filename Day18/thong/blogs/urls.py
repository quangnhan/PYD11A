from django.contrib import admin

from django.urls import path

from .views import BlogList, BlogCreate, BlogDetailView

urlpatterns = [
    path("", BlogList.as_view(), name="blog_list"),
    path("create", BlogCreate.as_view(), name="blog_create"),
    path("<int:pk>", BlogDetailView.as_view(), name="blog_create"),
]
