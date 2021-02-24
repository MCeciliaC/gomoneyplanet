# Generated by Django 3.1.5 on 2021-02-18 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20210218_0552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='clients',
        ),
        migrations.AddField(
            model_name='profile',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.seller', verbose_name='Vendedor asignado'),
        ),
    ]
