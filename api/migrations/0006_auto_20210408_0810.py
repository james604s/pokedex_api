# Generated by Django 3.1.3 on 2021-04-08 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210408_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokeevo',
            old_name='poke_number',
            new_name='poke_original',
        ),
        migrations.RenameField(
            model_name='poketype',
            old_name='poke_number',
            new_name='poke_original',
        ),
    ]