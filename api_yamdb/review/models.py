from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    title = models.ForeignKey(
        Titles,
        verbose_name='Произведения',
        on_delete=models.CASCADE,
        related_name='review',
    )
    author = models.ForeignKey(
        verbose_name='Author',
        on_delete=models.CASCADE,
        related_name='review'
    )
    text = models.TextField()
    raiting = models.FloatField(
        verbose_name='Rating',
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0),
        ])

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
