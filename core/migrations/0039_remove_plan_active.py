# Generated by Django 3.1.5 on 2021-03-03 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20210227_0249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='active',
        ),
    ]
