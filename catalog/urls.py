from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catalog.views import (products_list)

app_name = 'catalog'
urlpatterns = [
                path("admin/", admin.site.urls),
                path('', products_list, name='products_list'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


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
