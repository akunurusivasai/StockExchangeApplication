# Generated by Django 3.1.7 on 2021-05-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20210518_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='kycdetails',
            name='AadharPhoto',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kycdetails',
            name='PanPhoto',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='kycdetails',
            name='Signature',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
