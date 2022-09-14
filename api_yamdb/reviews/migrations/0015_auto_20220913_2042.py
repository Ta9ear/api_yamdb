# Generated by Django 2.2.16 on 2022-09-13 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_auto_20220913_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titlegenre',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Genres'),
        ),
        migrations.AlterField(
            model_name='titlegenre',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Titles'),
        ),
    ]
