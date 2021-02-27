# Generated by Django 3.1.5 on 2021-02-27 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20210226_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='invertion',
            field=models.IntegerField(blank=True, null=True, verbose_name='Inversión inicial'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tiempo total'),
        ),
        migrations.DeleteModel(
            name='Month',
        ),
        migrations.DeleteModel(
            name='Pay',
        ),
    ]