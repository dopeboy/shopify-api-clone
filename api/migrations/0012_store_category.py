# Generated by Django 3.1 on 2020-08-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200819_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='category',
            field=models.CharField(default='cat', max_length=200),
            preserve_default=False,
        ),
    ]
