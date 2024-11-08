from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


# Контроллеры

def contacts(request):
    return render(request, 'contacts.html') # Я без понятия зачем это мне


def home(request):
    return render(request, 'home.html') # И это тоже -_(:\)_-


class ProductListView(ListView):
    model = Product
    # catalog/Product_list.html


class ProductDetailView(DetailView):
    model = Product
    # catalog/Product_detail

class ProductCreateView(CreateView):
    # product_create
    model = Product
    form_class = ProductForm # Подключение формы ProductForm
    template_name = 'catalog/product_form.html' # шаблон
    success_url = reverse_lazy('catalog:product_list') # Перенаправляет на список продуктов после создания



class ProductUpdateView(UpdateView):
    # product_update
    model = Product
    form_class = ProductForm # Подключение формы ProductForm
    template_name = 'catalog/product_form.html' # шаблон
    success_url = reverse_lazy('catalog:product_form') # (?) а это нужно тут вообще?


    def get_success_url(self):
        # После редактирования возвращает на страницу (деталей) этого продукта, а не на product_list
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    # product_delete
    model = Product
    template_name = 'catalog/product_delete.html' # шаблон
    success_url = reverse_lazy('catalog:product_list') # Перенаправляет на список продуктов после удаления продукта



