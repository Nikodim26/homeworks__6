from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_TIMEOUT


def get_products_from_cache():
    products = cache.get("products_list")

    if products:
        return products
    products=Product.objects.filter(publication=True)
    cache.set("products_list", products, CACHE_TIMEOUT)
    return products

