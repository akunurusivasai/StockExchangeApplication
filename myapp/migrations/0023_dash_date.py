# Generated by Django 3.1.7 on 2021-05-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='dash',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
    ]