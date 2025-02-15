from .models import Product, Category

class CategoryService:

    @staticmethod
    def Products_in_category(category_id):
        products = Product.objects.filter(category_id=category_id)
        if not products.exists():
            return None

        return products
