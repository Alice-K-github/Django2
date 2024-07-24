from django.contrib import admin
from django.urls import path
from catalog.views import (product_list, contacts, home, product_detail)

app_name = 'catalog'
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', contacts),
    path('home/', home),
]

"""app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='students_list'),
]
"""

"""app_name = CatalogConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('home/', home),
    path('page/', page)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


                #path("", include(("catalog.urls", "catalog"), namespace="catalog")),

                #path('catalog', include('catalog.urls', 'catalog'), namespace='catalog')"""
