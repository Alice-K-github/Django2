from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    title = models.TextField(verbose_name='Заголовок', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='pictures/', verbose_name='Изображение(превью)', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Дата создания', help_text='формат "dd.mm.yy"', **NULLABLE)
    is_published = models.BooleanField(verbose_name='Признак публикации', **NULLABLE)
    views_counter = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0, **NULLABLE)

    def __str__(self):
        return f'{self.title} {self.content} {self.preview} {self.created_at} {self.is_published} {self.views_counter}'
