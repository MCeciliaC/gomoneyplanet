# Generated by Django 3.1.5 on 2021-02-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_delete_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['money'], 'verbose_name': 'Perfil Cliente', 'verbose_name_plural': 'Perfiles de Clientes'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='since',
        ),
        migrations.AddField(
            model_name='profile',
            name='money',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Dinero invertido'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='profile',
            name='start',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='days',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tiempo contrato'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gain',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Ganancia'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wallet',
            field=models.URLField(blank=True, default=None, max_length=500, null=True, verbose_name='Billetera'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de registro'),
        ),
    ]