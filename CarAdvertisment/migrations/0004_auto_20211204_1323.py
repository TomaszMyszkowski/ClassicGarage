# Generated by Django 3.2.8 on 2021-12-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarAdvertisment', '0003_auto_20211204_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_adveritsment',
            name='brand',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='car_adveritsment',
            name='model',
            field=models.CharField(max_length=30),
        ),
    ]
