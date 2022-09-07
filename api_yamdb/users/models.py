from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )
    role = models.CharField(verbose_name='role',
                            max_length=16,
                            choices=ROLE_CHOICES)
    email = models.EmailField(_('email address'),)

    def clean(self, *args, **kwargs) -> None:
        if self.is_superuser and self.role != 'admin':
            raise ValidationError('superuser must be admin!')
        return super().clean(**args, **kwargs)

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
