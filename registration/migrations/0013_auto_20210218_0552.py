# Generated by Django 3.1.5 on 2021-02-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20210218_0530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='seller',
        ),
        migrations.AddField(
            model_name='seller',
            name='clients',
            field=models.ManyToManyField(blank=True, null=True, to='registration.Profile', verbose_name='Clientes'),
        ),
    ]