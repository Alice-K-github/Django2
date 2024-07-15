from gettext import Catalog

from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category


# Контроллеры

def contacts(request):
    return render(request, 'contacts.html')


def home(request):
    return render(request, 'home.html')


# Create your views here.
def products_list(request):
    # product = Catalog.objects.get(pk=pk)
    # !!!
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def products_details(request, pk):
    # !!!
    product = get_object_or_404(Product, pk=pk)
    context = {"product":product}
    return render(request, 'products_ details.html', context)

