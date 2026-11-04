from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_TIMEOUT


def get_products_from_cache():
    products = cache.get("products_list")

    if not products is None:
        return products

    products = list(Product.objects.filter(publication=True))
    cache.set("products_list", products, CACHE_TIMEOUT)
    return products

def get_products_by_category(category_id: int):
    """Возвращает опубликованные товары категории через низкоуровневый кэш."""

    cache_key = f"category_{category_id}"
    products = cache.get(cache_key)

    if products is None:
        products = list(
            Product.objects.filter(
                category_id=category_id,
                publication=True,
            )
        )
        cache.set(cache_key, products, CACHE_TIMEOUT)

    return products