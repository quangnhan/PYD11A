from django.urls import path 
from .views import BlogListView, BlogCreateView, BlogDetailView

urlpatterns = [ 
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('create', BlogCreateView.as_view(),name='blog_create')
]
