# Generated by Django 5.0.7 on 2024-10-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, help_text='формат "dd.mm.yy"', null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views_counter',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Количество просмотров'),
        ),
    ]
