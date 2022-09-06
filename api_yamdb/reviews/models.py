from django.db import models


class Titles(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Name of the creation'
    )
    year = models.IntegerField(verbose_name='Create year')
    rating = models.IntegerField(verbose_name='Rating of the creation')
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
        related_name='category',
        verbose_name='Category of the creation'
    )

    def __str__(self):
        """
        Returns text of the Titles object
        """
        return self.name[:32]


class Genres(models.Model):
    name = models.CharField(max_length=256, verbose_name='Genre')
    slug = models.SlugField(
        unique=True, max_length=50, verbose_name='Slug of genre'
    )

    def __str__(self):
        """
        Returns text of the Genres object
        """
        return self.name[:32]


class Categories(models.Model):
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
    title = models.ForeignKey(Titles, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns title and genre names
        """
        return f'{self.title} {self.genre}'
