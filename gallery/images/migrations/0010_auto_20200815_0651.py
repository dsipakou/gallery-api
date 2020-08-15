# Generated by Django 3.0.3 on 2020-08-15 06:51

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_auto_20200705_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='date_created',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 15, 6, 50, 48, 259328, tzinfo=utc), verbose_name='picture date'),
        ),
    ]
