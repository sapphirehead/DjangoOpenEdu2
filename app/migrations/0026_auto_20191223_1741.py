# Generated by Django 2.2.6 on 2019-12-23 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20191223_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 23, 17, 41, 37, 78189), verbose_name='Publiced'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 23, 17, 41, 37, 78189), verbose_name='Date'),
        ),
    ]
