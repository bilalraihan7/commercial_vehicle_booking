# Generated by Django 4.2 on 2023-04-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiapp', '0005_driver_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='address',
            field=models.CharField(default='nothing', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='nothing', max_length=100),
        ),
    ]
