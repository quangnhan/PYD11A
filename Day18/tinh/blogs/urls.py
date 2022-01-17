from django.urls import path 
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

urlpatterns = [ 
    path('', BlogListView.as_view(), name='blog_list'),
    path('create', BlogCreateView.as_view(),name='blog_create'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name="blog_update"),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete')
]
