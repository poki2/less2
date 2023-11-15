import django_filters

from app.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ('price', 'categories', 'title')
