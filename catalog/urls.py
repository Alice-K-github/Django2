from django.contrib import admin
from django.urls import path
from catalog.views import (ProductListView, contacts, home, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, CategoryListView, CategoryCreateView, CategoryUpdateView,
                           CategoryDeleteView)

app_name = 'catalog' # Приложение

urlpatterns = [
    path("admin/", admin.site.urls), # Админка
    path('product/new/', ProductCreateView.as_view(), name='product_create'), # Создание продукта
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'), # Редактирование продукта
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'), # Удаление продукта
    path('', ProductListView.as_view(), name='product_list'), # Главная \ Список продуктов
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'), # Детали продукта
    path('contacts/', contacts),
    path('home/', home),


    path('category/', CategoryListView.as_view(), name='category_list'), # Главная \ Список категорий
    path('category/new/', CategoryCreateView.as_view(), name='category_create'), # Создание категории
    path('category/<int:pk>/update', CategoryUpdateView.as_view(), name='category_update'), # Редактирование категории
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'), # Удаление категории
]

