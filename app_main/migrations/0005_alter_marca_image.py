# Generated by Django 4.1.7 on 2023-03-29 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='image',
            field=models.ImageField(upload_to='marca_imgs/'),
        ),
    ]
