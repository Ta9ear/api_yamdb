# Generated by Django 2.2.16 on 2022-09-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_auto_20220916_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
