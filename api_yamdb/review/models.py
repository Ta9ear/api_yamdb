from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    title = models.ForeignKey(
        Titles,
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
        ordering = ['pub_date']
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
        ordering = ['pub_date']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
