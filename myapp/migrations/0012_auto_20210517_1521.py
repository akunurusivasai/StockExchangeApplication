# Generated by Django 3.1.7 on 2021-05-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_wallet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='name',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
