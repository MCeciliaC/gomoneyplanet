# Generated by Django 3.1.5 on 2021-03-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0049_auto_20210303_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='client_active',
            field=models.BooleanField(default=True, verbose_name='Cliente activo'),
        ),
    ]
