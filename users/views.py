from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView

from config.settings import EMAIL_HOST_USER
from users.forms import CustomUserCreationForm


def home(request):
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')


class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('home')


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

