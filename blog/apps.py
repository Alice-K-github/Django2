from django.apps import AppConfig

# Указание данного приложения
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
