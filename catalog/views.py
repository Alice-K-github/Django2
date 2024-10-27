from gettext import Catalog
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category

from django.views.generic import ListView, DetailView


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

