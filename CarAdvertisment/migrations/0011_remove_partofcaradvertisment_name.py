# Generated by Django 4.0 on 2021-12-08 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarAdvertisment', '0010_auto_20211206_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partofcaradvertisment',
            name='name',
        ),
    ]
