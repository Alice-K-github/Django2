from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, CategoryForm, ProductModeratorForm
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
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    # product_update
    model = Product
    form_class = ProductForm # Подключение формы ProductForm
    template_name = 'catalog/product_form.html' # шаблон
    success_url = reverse_lazy('catalog:product_form') # (?) а это нужно тут вообще?
    permission_required = 'catalog.change_product'


    def get_success_url(self):
        # После редактирования возвращает на страницу (деталей) этого продукта, а не на product_list
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


    def form_valid(self, form):
        # Автоматическое добавление даты редактирования продукта
        form.instance.updated_at = datetime.now()
        return super().form_valid(form)


    def get_form_class(self):
            user = self.request.user
            if user == self.object.owner:
                return ProductForm
            if user.has_perm('catalog.can_unpublish_product'):
                return ProductModeratorForm
            raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    # product_delete
    model = Product
    template_name = 'catalog/product_delete.html' # шаблон
    success_url = reverse_lazy('catalog:product_list') # Перенаправляет на список продуктов после удаления продукта
    permission_required = 'catalog.delete_product'

    def get_form_class(self):
        user = self.request.user
        if not user.has_perm('catalog.delete_product') or not user == self.object.owner:
            raise PermissionDenied

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


