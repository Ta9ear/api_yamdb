# Generated by Django 2.2.16 on 2022-09-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20220913_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='genre',
            field=models.ManyToManyField(through='reviews.TitleGenre', to='reviews.Genres', verbose_name='Genry of the creation'),
        ),
    ]
