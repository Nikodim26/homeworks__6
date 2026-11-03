from catalog.models import Category, Product


class ProductService:

    @staticmethod
    def get_categories():
        return Category.objects.all()

    @staticmethod
    def get_products_list(pk):
        return Product.objects.filter(category_id=pk)