# Generated by Django 3.1.7 on 2021-05-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20210518_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='kycdetails',
            name='UserPhoto',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='kycdetails',
            name='PhNumber',
            field=models.IntegerField(max_length=10),
        ),
    ]