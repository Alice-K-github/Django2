from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    # Категории продуктов
    name = models.CharField(max_length=150, verbose_name='Наименование', **NULLABLE)
    description = models.CharField(max_length=150, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'наименование категории'  # Настройка для наименования одного объекта
        verbose_name_plural = 'наименования категорий'  # Настройка для наименования набора объектов



class Product(models.Model):
    #  Продукты
    name = models.CharField(max_length=150, verbose_name='Наименование', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    picture = models.ImageField(upload_to='media/', verbose_name='Изображение(превью)', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Дата создания записи в БД', **NULLABLE)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения записи в БД', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufactured_at = models.DateTimeField(verbose_name='Дата производства продукта', **NULLABLE, default='False')
    is_publicated = models.BooleanField(verbose_name="Статус публикации", **NULLABLE)



    def __str__(self):
        return f'{self.name} {self.description} {self.picture} {self.category} {self.price} {self.created_at} {self.updated_at} {self.manufactured_at}'

    class Meta:
        verbose_name = 'наименование продукта'  # Настройка для наименования одного объекта
        verbose_name_plural = 'наименования продуктов'  # Настройка для наименования набора объектов
        permissions  = [
            ('can_unpublish_product', 'can unpublish product')
        ]

