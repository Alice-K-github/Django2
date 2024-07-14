from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", include("catalog.urls", namespace="catalog")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
#
# def static(MEDIA_URL, document_root):
#     pass
#
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
