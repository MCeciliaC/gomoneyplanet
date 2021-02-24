# Generated by Django 3.1.5 on 2021-02-12 16:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('text', ckeditor.fields.RichTextField(max_length=200, verbose_name='Desarrollo')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
            ],
            options={
                'verbose_name': 'Pregunta frecuente',
                'ordering': ['order'],
            },
        ),
    ]