# Generated by Django 3.1 on 2020-08-15 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hero',
            new_name='User',
        ),
    ]