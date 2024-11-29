from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(verbose_name="Аватар", upload_to='pictures/', blank=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15, blank=True, help_text='Введите номер телефона (необязательно)')
    country = models.CharField(verbose_name='Страна', max_length=30, blank=True, help_text="Введите страну (необязательно)")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


