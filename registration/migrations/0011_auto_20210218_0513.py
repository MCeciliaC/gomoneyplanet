# Generated by Django 3.1.5 on 2021-02-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20210218_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='staff',
            field=models.BooleanField(default=True),
        ),
    ]
