# Generated by Django 3.2.9 on 2021-12-06 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarAdvertisment', '0009_auto_20211206_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caradveritsment',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='caradveritsment',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='caradveritsment',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='partofcaradvertisment',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='partofcaradvertisment',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='partofcaradvertisment',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='serviceadvertisment',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='serviceadvertisment',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='serviceadvertisment',
            name='modified_date',
        ),
    ]
