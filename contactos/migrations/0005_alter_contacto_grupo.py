# Generated by Django 4.1.1 on 2022-12-29 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0004_grupo_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='grupo',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='contactos.grupo'),
        ),
    ]