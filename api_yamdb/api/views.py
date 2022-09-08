from rest_framework import filters, viewsets
from reviews.models import Categories, Genres, Titles

from api.permissions import IsAdminOrReadOnly
from api.serializers import (CategoriesSerializer, GenresSerializer,
                             TitlesReadSerializer, TitlesWriteSerializer)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'genre', 'category', 'year')
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitlesReadSerializer
        return TitlesWriteSerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'
