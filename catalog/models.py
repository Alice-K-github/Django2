from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'наименование'  # Настройка для наименования одного объекта
        verbose_name_plural = 'наименования'  # Настройка для наименования набора объектов
        # verbose_description = 'описание'
        # verbose_description_plural = 'описания'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    picture = models.ImageField(upload_to='pictures/', verbose_name='Изображение(превью)', **NULLABLE)
    category = models.CharField(max_length=500, verbose_name='Категория', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='Дата создания записи в БД', **NULLABLE)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения записи в БД', **NULLABLE)
    сategory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.description} {self.picture} {self.category} {self.price} {self.data_first} {self.data_last}'

    class Meta:
        verbose_name = 'наименование'  # Настройка для наименования одного объекта
        verbose_name_plural = 'наименования'  # Настройка для наименования набора объектов
        # verbose_description = 'описание'
        # verbose_description_plural = 'описания'
        # verbose_picture = 'изображение'
        # verbose_picture_plural = 'изображения'
        # verbose_category = 'категория'
        # verbose_category_plural = 'категории'
        # verbose_price = 'цена'
        # verbose_price_plural = 'цены'
        # verbose_created_at = 'дата'
        # verbose_created_at_plural = 'даты'
        # verbose_updated_at = 'дата'
        # verbose_updated_at_plural = 'даты'
