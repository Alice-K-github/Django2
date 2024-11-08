from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


# Контроллеры

def contacts(request):
    return render(request, 'contacts.html')


def home(request):
    return render(request, 'home.html')


class ProductListView(ListView):
    model = Product
    # catalog/Product_list.html


class ProductDetailView(DetailView):
    model = Product
    # catalog/Product_detail

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_form')

    def get_success_url(self):
        # После редактирования возвращает на страницу (деталей) этого продукта, а не на product_list
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:product_list')



