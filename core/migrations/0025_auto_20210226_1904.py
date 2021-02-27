# Generated by Django 3.1.5 on 2021-02-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20210226_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='invertion',
            field=models.IntegerField(blank=True, null=True, verbose_name='Inversion inicial'),
        ),
        migrations.AddField(
            model_name='plan',
            name='percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Porcentaje mensual'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
