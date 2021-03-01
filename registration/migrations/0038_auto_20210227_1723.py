# Generated by Django 3.1.5 on 2021-02-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20210227_0249'),
        ('registration', '0037_auto_20210227_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='currency',
        ),
        migrations.AddField(
            model_name='profile',
            name='currency',
            field=models.ManyToManyField(blank=True, null=True, to='core.Currency'),
        ),
    ]
