# Generated by Django 3.1.5 on 2021-02-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0027_auto_20210221_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='active',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='active',
        ),
        migrations.AddField(
            model_name='profile',
            name='client_active',
            field=models.BooleanField(default=False, verbose_name='Cliente activo'),
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_active',
            field=models.BooleanField(default=False, verbose_name='Vendedor activo'),
        ),
    ]