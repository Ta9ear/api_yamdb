import datetime as dt

from django.db.models import Avg
from rest_framework import serializers
from reviews.models import Comment, Review, Categories, Genres, Titles
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator


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


class GenresSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Genres.objects.all())]
    )
    slug = serializers.CharField(
        validators=[UniqueValidator(queryset=Genres.objects.all())]
    )

    class Meta:
        model = Genres
        fields = ('name', 'slug')


class CategoriesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Categories.objects.all())]
    )
    slug = serializers.CharField(
        validators=[UniqueValidator(queryset=Categories.objects.all())]
    )

    class Meta:
        model = Categories
        fields = ('name', 'slug')


class TitlesReadSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    genre = GenresSerializer(many=True)
    category = CategoriesSerializer()

    class Meta:
        model = Titles
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')

    def get_rating(self, obj):
        return obj.reviews.aggregate(Avg('score')).get('score__avg')


class TitlesWriteSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genres.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Categories.objects.all()
    )

    class Meta:
        model = Titles
        fields = ('name', 'year', 'description', 'genre', 'category')

    def validate_year(self, value):
        current_year = dt.date.today().year
        if value > current_year:
            raise serializers.ValidationError('Check the year of creation')
        return value
