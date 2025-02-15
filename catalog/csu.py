from django.core.management import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(email="admin@example.ru")
        user.set_password("123123")
        user.is_stuff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
