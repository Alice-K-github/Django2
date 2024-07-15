from django.core.management import BaseCommand
import json
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        # Здесь мы получаем данные из фикстурв с категориями
        categories_json = open("categories.json")
        json.load(categories_json)
        return categories_json

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстурв с продуктами
        products_json = open("products.json")
        json.load(products_json)
        return products_json

    def handle(self, *args, **options):

        # products_json = self.json_read_products()
        # categories_json = self.json_read_categories()
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

                # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

                # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['name'], description=category['description']))

                # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

                # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product["name"], description=product["description"], picture=product["picture"], price=product["price"], created_at=product["created_at"], updated_at=product["updated_at"],
                                                # получаем категорию из базы данных для корректной связки объектов
                        category=Category.objects.get(pk=product["pk"]))
            )

                # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)