from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    )

    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='first_name',
        blank=True,
        null=True,
        default=None,
        max_length=150
    )
    last_name = models.CharField(
        verbose_name='last_name',
        max_length=150,
        blank=True,
        null=True,
        default=None
    )
    bio = models.TextField(
        verbose_name='biograthy',
        blank=True,
        null=True,
        default=None
    )
    role = models.CharField(
        verbose_name='role',
        max_length=16,
        choices=ROLE_CHOICES,
        default=USER
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=254,
        unique=True
    )
    password = None

    class Meta:
        ordering = ['username']

    def clean(self) -> None:
        if self.is_superuser:
            self.role = 'admin'
        return super().clean()

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    @property
    def is_admin(self):
        if self.role == 'admin':
            return True
        return False

    @property
    def is_moderator(self):
        if self.role == 'moderator':
            return True
        return False
