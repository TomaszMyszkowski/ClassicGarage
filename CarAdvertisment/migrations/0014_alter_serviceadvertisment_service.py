# Generated by Django 3.2.8 on 2021-12-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarAdvertisment', '0013_auto_20211211_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceadvertisment',
            name='service',
            field=models.CharField(choices=[('lakierowanie', 'lakierowanie'), ('blacharstwo', 'blacharstwo'), ('mechanika', 'mechanika')], max_length=12),
        ),
    ]
