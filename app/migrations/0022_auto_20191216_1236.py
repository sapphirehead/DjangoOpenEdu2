# Generated by Django 2.2.6 on 2019-12-16 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20191216_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 16, 12, 36, 20, 751024), verbose_name='Publiced'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 12, 16, 12, 36, 20, 752025), verbose_name='Date'),
        ),
    ]
