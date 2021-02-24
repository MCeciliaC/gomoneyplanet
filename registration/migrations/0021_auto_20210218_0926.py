# Generated by Django 3.1.5 on 2021-02-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0020_auto_20210218_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='urlbutton',
            field=models.URLField(blank=True, default=None, max_length=500, null=True, verbose_name='Link Paypal'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='paybutton',
            field=models.BooleanField(default=False, verbose_name='Botón de pago'),
        ),
    ]