from gettext import Catalog

from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category


# Контроллеры

def contacts(request):
    return render(request, 'contacts.html')


def home(request):
    return render(request, 'home.html')


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    # должен быть object_list для прохождение в цикле по всем продуктам
    context = {"object_list": products}
    return render(request, "product_list.html", context)


def product_detail(request, pk):
    # !!!
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)
