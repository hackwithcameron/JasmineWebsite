# Generated by Django 3.0.3 on 2020-05-13 22:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_auto_20200513_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodblogpost',
            name='post',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
