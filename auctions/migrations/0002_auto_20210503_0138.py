# Generated by Django 2.2.12 on 2021-05-03 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='listing',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='users',
            field=models.IntegerField(default=None, null=True),
        ),
    ]