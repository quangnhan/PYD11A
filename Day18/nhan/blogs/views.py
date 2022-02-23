from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.contrib.auth.models import User
from .models import Blog
from .forms import BlogCreationForm
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
    context_object_name = "blog"

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blogs/blog_update.html"
    fields = ('name', 'content', 'status', 'author')

    def get_success_url(self, **kwargs):
        blog = self.get_object()
        return reverse_lazy('blog_detail', args=(blog.id,))

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "blogs/blog_delete.html"
    context_object_name = "blog"

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog_list')

class BlogCreateView2(FormView):
    form_class = BlogCreationForm
    success_url = reverse_lazy('blog_list')
    template_name = 'blogs/blog_create.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        name = form.cleaned_data['name']
        content = form.cleaned_data['content']
        status = form.cleaned_data['status']
        author_id = form.cleaned_data['author']

        # Get author from database
        user = User.objects.get(pk=author_id)

        # Create new user
        Blog.objects.create(name=name, content=content, status=status, author=user)

        return super().form_valid(form)