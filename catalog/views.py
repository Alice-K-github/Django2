from gettext import Catalog

from django.shortcuts import render

from catalog.models import Product, Category


# Контроллеры

# Create your views here.
def index(request):
    #product = Catalog.objects.get(pk=pk)
    product = Category.objects.all()
    context = {'product': product}
    return render(request, 'catalog/page.html', context)
