# Generated by Django 3.2.8 on 2021-12-04 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarAdvertisment', '0002_auto_20211204_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part_of_car_advertisment',
            old_name='user',
            new_name='id_user',
        ),
        migrations.RenameField(
            model_name='service_advertisment',
            old_name='user',
            new_name='id_user',
        ),
    ]
