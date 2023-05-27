# Generated by Django 4.2 on 2023-05-23 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiapp', '0016_alter_driver_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=25)),
                ('amount', models.IntegerField()),
                ('cardno', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('bookid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiapp.booking')),
            ],
        ),
    ]
