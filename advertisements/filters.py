from unicodedata import name
from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    creator = filters.NumberFilter(lookup_expr='exact')
    created_at = filters.DateFromToRangeFilter()
    # created_at_after = filters.DateFromToRangeFilter(
    #     field_name='created_at', lookup_expr='created_at_after', name="created_at_after")

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at']
