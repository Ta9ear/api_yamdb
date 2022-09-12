from rest_framework import serializers
from reviews.models import Comment, Review
from rest_framework.validators import UniqueTogetherValidator, UniqueConstraint


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='user',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field='username',
        read_only=True,
    )

    class Meta:
        fields = '__all__'
        model = Review
        constraints = [
            UniqueConstraint(fields=['author', 'title'], name='rating_once'),
        ]
        validators = [UniqueTogetherValidator(queryset=Review.objects.all(),
                                              fields=['title', 'author'])]

    def validate(self, data):
        author = self.context['request'].user
        if data['author'] == author:
            if Review.objects.filter(author=author).exists():
                raise serializers.ValidationError(
                    'Один отзыв на пользователя к произведению!')
                return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment
