# Generated by Django 2.2.12 on 2021-04-10 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210403_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='bidder',
            field=models.CharField(default='no bidders', max_length=20, null=True),
        ),
    ]