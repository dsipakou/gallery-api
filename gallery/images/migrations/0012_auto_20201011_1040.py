# Generated by Django 3.0.3 on 2020-10-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_auto_20201001_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(verbose_name='picture date'),
        ),
    ]
