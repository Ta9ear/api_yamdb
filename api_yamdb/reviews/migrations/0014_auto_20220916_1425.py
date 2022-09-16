# Generated by Django 2.2.16 on 2022-09-16 11:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_auto_20220916_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
