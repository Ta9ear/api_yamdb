from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class User(AbstractUser):

    username = models.CharField(verbose_name='username',
                                max_length=150,
                                unique=True)
    first_name = models.CharField(verbose_name='first_name',
                                  blank=True,
                                  max_length=150)
    last_name = models.CharField(verbose_name='last_name',
                                 max_length=150,
                                 blank=True)
    bio = models.TextField(verbose_name='biograthy', blank=True)
    role = models.CharField(verbose_name='role',
                            max_length=16,
                            choices=ROLE_CHOICES)
    email = models.EmailField(verbose_name='email',
                              max_length=254,
                              unique=True)
    password = None

    def clean(self, *args, **kwargs) -> None:
        if self.is_superuser:
            self.role = 'admin'
        return super().clean(**args, **kwargs)

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
