# Generated by Django 4.1.4 on 2022-12-27 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listar',
            old_name='addres',
            new_name='last_name',
        ),
    ]
