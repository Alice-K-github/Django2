from django.contrib import admin
from django.urls import path
from catalog.views import (ProductListView, contacts, home, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView)

app_name = 'catalog' # Приложение

urlpatterns = [
    path("admin/", admin.site.urls), # Админка
    path('product/new/', ProductCreateView.as_view(), name='product_create'), # Создание
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'), # Редактирование
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'), # Удаление
    path('', ProductListView.as_view(), name='product_list'), # Главная \ Список продуктов
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'), # Детали продукта
    path('contacts/', contacts),
    path('home/', home),
]

