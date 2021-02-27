# Generated by Django 3.1.5 on 2021-02-26 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210226_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'ordering': ['invertion'], 'verbose_name': 'Plan disponible', 'verbose_name_plural': 'Planes disponibles'},
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='initial',
            new_name='invertion',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='three',
            new_name='time1',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='six',
            new_name='time2',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='twelve',
            new_name='time3',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='order',
        ),
    ]
