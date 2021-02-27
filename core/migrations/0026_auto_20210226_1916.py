# Generated by Django 3.1.5 on 2021-02-26 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20210226_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='Costos planes')),
                ('payment', models.IntegerField(blank=True, null=True, verbose_name='Costo plan en euros')),
                ('paybutton', models.BooleanField(default=False, verbose_name='Botón de pago')),
                ('urlbutton', models.URLField(blank=True, default=None, max_length=500, null=True, verbose_name='Link Paypal')),
            ],
            options={
                'verbose_name_plural': 'Costos planes',
                'ordering': ['payment'],
            },
        ),
        migrations.RemoveField(
            model_name='plan',
            name='paybutton',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='urlbutton',
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Número de plan'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.month', verbose_name='Meses'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='invertion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.pay', verbose_name='Costo plan'),
        ),
    ]