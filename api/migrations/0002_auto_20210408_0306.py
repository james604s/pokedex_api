# Generated by Django 3.1.3 on 2021-04-08 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='pokeevo',
            table='poke_evo',
        ),
        migrations.AlterModelTable(
            name='pokeinfo',
            table='poke_info',
        ),
        migrations.AlterModelTable(
            name='poketype',
            table='poke_type',
        ),
    ]
