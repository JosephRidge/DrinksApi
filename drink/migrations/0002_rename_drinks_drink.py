# Generated by Django 4.1 on 2022-08-08 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drinks',
            new_name='Drink',
        ),
    ]
