# Generated by Django 2.2.12 on 2021-04-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_listings_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='commenter',
            field=models.CharField(max_length=20, null=True),
        ),
    ]