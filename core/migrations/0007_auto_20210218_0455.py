# Generated by Django 3.1.5 on 2021-02-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210217_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]