# Generated by Django 5.0.7 on 2024-07-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Дата производства продукта'),
        ),
    ]
