# Generated by Django 2.2.16 on 2022-09-16 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220916_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='text',
            new_name='field',
        ),
    ]
