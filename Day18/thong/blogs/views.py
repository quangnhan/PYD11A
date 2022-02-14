# from django.shortcuts import render
# from django.views.generic import TemplateView

from django.views.generic import ListView, DetailView
from .models import Blog
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class BlogList(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "list_blog"


class BlogCreate(CreateView):
    model = Blog
    template_name = "blog/blog_create.html"
    fields = ("name", "content", "status")

    def get_success_url(self, **kwargs):
        return reverse_lazy("blog_list")


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"
