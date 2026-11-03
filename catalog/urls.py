from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, CatalogueView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),

    path('product/<int:pk>/',cache_page(60)(ProductDetailView.as_view()), name='product'),

    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_list/<int:category_pk>/', ProductListView.as_view(), name='product_list'),


]
