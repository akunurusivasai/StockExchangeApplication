# Generated by Django 3.1.7 on 2021-05-19 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20210519_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dash',
            old_name='Date',
            new_name='date',
        ),
    ]