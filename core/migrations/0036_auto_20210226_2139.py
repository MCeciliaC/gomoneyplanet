# Generated by Django 3.1.5 on 2021-02-27 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20210226_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='tag',
            field=models.CharField(default='<i class="fas fa-redo"></i>', max_length=100, verbose_name='Ícono'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Duración en meses'),
        ),
    ]