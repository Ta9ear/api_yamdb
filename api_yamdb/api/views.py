from django.shortcuts import get_object_or_404
from reviews.models import Review, Title
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from .serializers import ReviewSerializer, CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        get_object_or_404(Title, pk=self.kwargs.get('Title_id'))
        serializer.save(author=self.request.user)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('Title_id'))
        return title.reviews.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, title=title_id)
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()
