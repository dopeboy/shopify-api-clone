# Generated by Django 3.1 on 2020-08-16 00:52

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200815_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='products',
            field=jsonfield.fields.JSONField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='preferences',
            field=models.CharField(max_length=1000),
        ),
    ]