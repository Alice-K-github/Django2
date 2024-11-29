from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from users.forms import CustomUserCreationForm


def home(request):
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home.html')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class RegisterView(View):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

