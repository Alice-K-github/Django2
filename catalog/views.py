from datetime import datetime
from itertools import product

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category
from django.conf import settings
from django.shortcuts import render



# Контроллеры


def Badwords_view(request):
    context = {
        'bad_words': settings.bad_words,
    }
    return render(request, 'bad_words.html', context)


def contacts(request):
    return render(request, 'contacts.html') # Я без понятия зачем это мне


def home(request):
    return render(request, 'home.html')


class ProductListView(ListView):
    model = Product
    # catalog/Product_list.html


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    # catalog/Product_detail


class ProductCreateView(LoginRequiredMixin, CreateView):
    # product_create
    model = Product
    form_class = ProductForm # Подключение формы ProductForm
    template_name = 'catalog/product_form.html' # шаблон
    success_url = reverse_lazy('catalog:product_list') # Перенаправляет на список продуктов после создания

    def form_valid(self, form):
        # Автоматическое добавление даты создания продукта
        form.instance.created_at = datetime.now()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    # product_update
    model = Product
    form_class = ProductForm # Подключение формы ProductForm
    template_name = 'catalog/product_form.html' # шаблон
    success_url = reverse_lazy('catalog:product_form') # (?) а это нужно тут вообще?


    def get_success_url(self):
        # После редактирования возвращает на страницу (деталей) этого продукта, а не на product_list
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


    def form_valid(self, form):
        # Автоматическое добавление даты редактирования продукта
        form.instance.updated_at = datetime.now()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    # product_delete
    model = Product
    template_name = 'catalog/product_delete.html' # шаблон
    success_url = reverse_lazy('catalog:product_list') # Перенаправляет на список продуктов после удаления продукта


# Категории



class CategoryListView(ListView):
    model = Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm  # Подключение формы CategoryForm
    template_name = 'catalog/category_form.html'  # шаблон
    success_url = reverse_lazy('catalog:category_list')  # Перенаправляет на список категорий после создания


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    # category_update
    model = Category
    form_class = CategoryForm # Подключение формы CategoryForm
    template_name = 'catalog/category_form.html' # шаблон
    success_url = reverse_lazy('catalog:category_list') # Перенаправляет на список категорий после создания


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    # product_delete
    model = Category
    template_name = 'catalog/category_delete.html' # шаблон
    success_url = reverse_lazy('catalog:category_list') # Перенаправляет на список категорий после удаления продукта


