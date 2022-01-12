from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Blog

# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "list_blog"

class BlogCreateView(CreateView):
    model = Blog
    template_name = "blogs/blog_create.html"
    fields = ('name', 'content', 'status')

    def get_success_url(self, **kwargs):      
        return reverse_lazy('blog_list')
