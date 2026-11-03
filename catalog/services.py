from catalog.models import Category


class ProductService:

    @staticmethod
    def get_categories():
        return Category.objects.all()

    @staticmethod
    def get_products_list():
        return ['a','b','c']