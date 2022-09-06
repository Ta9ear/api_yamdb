from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    title = models.ForeignKey(
        Titles,
        verbose_name='Productions',
        on_delete=models.CASCADE,
        related_name='Review',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.CASCADE,
        related_name='Review'
    )
    text = models.TextField()
    score = models.IntegerField(
        verbose_name='Rating',
        validators=[
            MinValueValidator[0],
            MaxValueValidator[10],
        ])
    pub_date = models.DateTimeField(
        verbose_name='Date of publication',
        auto_now_add=True
    )

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
