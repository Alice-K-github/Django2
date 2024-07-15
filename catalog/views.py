from gettext import Catalog

from django.shortcuts import render

from catalog.models import Product, Category


# Контроллеры

# Create your views here.
def products_list(request):
    #product = Catalog.objects.get(pk=pk)
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)
