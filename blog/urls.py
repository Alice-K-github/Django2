from django.contrib import admin
from django.urls import path
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, base

app_name = 'blog'
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('base/', base, name='base'),
]

