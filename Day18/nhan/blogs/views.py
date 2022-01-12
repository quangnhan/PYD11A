from django.views.generic import ListView
from .models import Blog

# Create your views here.

class BlogList(ListView):
    model = Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "list_blog"
