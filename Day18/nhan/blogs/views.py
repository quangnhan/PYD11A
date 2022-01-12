from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class BlogList(TemplateView):
    template_name = "blogs/blog_list.html"
