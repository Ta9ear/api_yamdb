from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from reviews.models import Categories, Genres, Titles

from api.filters import CategoriesFilter, GenresFilter, TitlesFilter
from api.mixins import CreateListDestroyViewSet
from api.permissions import IsAdminOrReadOnly
from api.serializers import (CategoriesSerializer, GenresSerializer,
                             TitlesReadSerializer, TitlesWriteSerializer)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitlesFilter
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitlesReadSerializer
        return TitlesWriteSerializer


class GenresViewSet(CreateListDestroyViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GenresFilter
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class CategoriesViewSet(CreateListDestroyViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoriesFilter
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'
