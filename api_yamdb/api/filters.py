import django_filters.rest_framework as d_filters

from reviews.models import Titles


class TitlesFilter(d_filters.FilterSet):
    name = d_filters.CharFilter(field_name='name', lookup_expr='icontains')
    year = d_filters.NumberFilter(field_name='year')
    genre = d_filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='icontains',
    )
    category = d_filters.CharFilter(
        field_name='category__slug',
        lookup_expr='icontains',
    )

    class Meta:
        model = Titles
        fields = ['name', 'year', 'genre', 'category']
