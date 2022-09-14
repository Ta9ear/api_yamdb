from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint
from users.models import User


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Name of the creation'
    )
    year = models.IntegerField(verbose_name='Create year')
    description = models.TextField(
        max_length=1024,
        verbose_name='Description of the creation',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        'Genres',
        through='TitleGenre'
    )
    category = models.ForeignKey(
        'Categories',
        on_delete=models.SET_NULL,
        null=True,
        related_name='category',
        verbose_name='Category of the creation'
    )

    def __str__(self):
        """
        Returns text of the Titles object
        """
        return self.name[:32]


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='Genre')
    slug = models.SlugField(
        unique=True, max_length=50, verbose_name='Slug of genre'
    )

    def __str__(self):
        """
        Returns text of the Genres object
        """
        return self.name[:32]


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Category')
    slug = models.SlugField(
        unique=True, max_length=50, verbose_name='Slug of category'
    )

    def __str__(self):
        """
        Returns text of the Categories object
        """
        return self.name[:32]


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns title and genre names
        """
        return f'{self.title} {self.genre}'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Productions',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    score = models.IntegerField(
        verbose_name='Rating',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ])
    pub_date = models.DateTimeField(
        verbose_name='Date of publication',
        auto_now_add=True
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=['author', 'title'], name='rating_once'),
        ]
        ordering = ['-pub_date']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        verbose_name='Date of publication',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
