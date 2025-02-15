from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from users.views import home, RegisterView, CustomLogoutView

app_name = 'users' # Приложение

urlpatterns = [
        path("admin/", admin.site.urls), # Админка
        path('', home),
        path("logout/", LogoutView.as_view(next_page='/catalog/'), name="logout"),
        path('login/', LoginView.as_view(), name='login'),
        path('register/', RegisterView.as_view(), name='register'),
        path('accounts/', include('django.contrib.auth.urls'))
    ]
