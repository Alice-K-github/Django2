# coding: utf-8
from users.models import CustomUser
user = CustomUser.objects.get(username='admin@example.ru')
CustomUser.objects.create_superuser('admin@example.ru', '123123')
CustomUser.objects.create_superuser('admin', 'admin@example.ru', '123123')
