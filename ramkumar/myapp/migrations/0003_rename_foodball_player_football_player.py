# Generated by Django 4.2.6 on 2023-11-08 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_foodball_player_delete_employee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='foodball_player',
            new_name='football_player',
        ),
    ]
