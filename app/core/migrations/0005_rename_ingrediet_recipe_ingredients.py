# Generated by Django 3.2.19 on 2023-07-01 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230701_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingrediet',
            new_name='ingredients',
        ),
    ]
