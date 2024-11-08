from django.contrib import admin
from django.urls import path
from catalog.views import (ProductListView, contacts, home, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView)

app_name = 'catalog'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', contacts),
    path('home/', home),
]

