# Generated by Django 3.1.7 on 2021-05-12 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210511_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocks',
            name='img',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='price',
        ),
    ]
