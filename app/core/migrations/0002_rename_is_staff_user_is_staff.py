# Generated by Django 3.2.13 on 2022-04-21 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_Staff',
            new_name='is_staff',
        ),
    ]
