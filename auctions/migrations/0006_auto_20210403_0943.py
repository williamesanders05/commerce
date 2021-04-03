# Generated by Django 2.2.12 on 2021-04-03 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210403_0914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='listings',
        ),
        migrations.AddField(
            model_name='listings',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='auctions.Categories'),
        ),
    ]
