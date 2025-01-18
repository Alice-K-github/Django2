from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
                  path("admin/", admin.site.urls), # Подключение связки
                  path("catalog/", include("catalog.urls", namespace="catalog")), # Приложение "catalog"
                  path("blog/", include("blog.urls", namespace="blog")), # Приложение "blog"
                  path("users/", include("users.urls", namespace="users")) # Приложение "users"
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Подключение статики


