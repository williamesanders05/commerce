# Generated by Django 2.2.12 on 2021-04-24 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20210423_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='close',
            field=models.BooleanField(default=False),
        ),
    ]