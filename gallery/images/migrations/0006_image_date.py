# Generated by Django 3.0.3 on 2020-06-03 16:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20200512_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 16, 36, 43, 694476, tzinfo=utc), verbose_name='picture date'),
        ),
    ]
