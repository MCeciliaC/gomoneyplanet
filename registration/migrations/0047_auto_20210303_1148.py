# Generated by Django 3.1.5 on 2021-03-03 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0046_auto_20210302_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Nombre de usuario'),
        ),
    ]
