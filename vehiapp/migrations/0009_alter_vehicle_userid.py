# Generated by Django 4.1.7 on 2023-04-20 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiapp', '0008_vehicle_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiapp.driver'),
        ),
    ]
