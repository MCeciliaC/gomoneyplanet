# Generated by Django 3.1.5 on 2021-02-16 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210215_2105'),
        ('registration', '0008_auto_20210215_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='currencys',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.currency'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='clients',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.profile'),
        ),
    ]
