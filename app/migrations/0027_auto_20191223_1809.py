# Generated by Django 2.2.6 on 2019-12-23 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20191223_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 23, 18, 9, 8, 750317), verbose_name='Publiced'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 23, 18, 9, 8, 750317), verbose_name='Date'),
        ),
    ]
