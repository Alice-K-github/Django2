from django.shortcuts import render


# Контроллеры

# Create your views here.
def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


def page(request):
    return render(request, 'catalog/page.html')
