from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from reviews.models import Categories, Genres, Review, Titles

from api.filters import CategoriesFilter, GenresFilter, TitlesFilter
from api.mixins import CreateListDestroyViewSet
from api.permissions import IsAdminModeratorAuthorOrReadOnly, IsAdminOrReadOnly
from api.serializers import (CategoriesSerializer, CommentSerializer,
                             GenresSerializer, ReviewSerializer,
                             TitlesReadSerializer, TitlesWriteSerializer)

from django.db.models import Avg


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsAdminModeratorAuthorOrReadOnly,)

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Titles, pk=self.kwargs.get('title_id'))
        return title.reviews.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAdminModeratorAuthorOrReadOnly,)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get("review_id"))
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id, title=title_id)
        serializer.save(author=self.request.user, review=review)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all().annotate(
        Avg("reviews__score")
    ).order_by("name")
    serializer_class = TitlesReadSerializer
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
