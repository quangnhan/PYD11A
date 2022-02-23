from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from .models import Blog

# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "list_blog"

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "blogs/blog_create.html"
    fields = ('name', 'content', 'status', 'author')

    def get_success_url(self, **kwargs):      
        return reverse_lazy('blog_list')


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"
    context_object_name  = "blog"

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blogs/blog_update.html"
    fields = ["name", "content", "status"]
    
    def get_success_url(self, **kwargs):
        blog = self.get_object()
        return reverse_lazy('blog_detail', args=(blog.id,))

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = "blogs/blog_delete.html"
    context_object_name = "blog"

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog_list')
