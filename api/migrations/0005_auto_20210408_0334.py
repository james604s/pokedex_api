# Generated by Django 3.1.3 on 2021-04-08 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210408_0327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokeevo',
            old_name='poke_info',
            new_name='poke_number',
        ),
        migrations.RenameField(
            model_name='poketype',
            old_name='poke_info',
            new_name='poke_number',
        ),
    ]
