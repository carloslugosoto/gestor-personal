# Generated by Django 4.1.1 on 2022-12-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactos', '0003_alter_contacto_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='nombre',
            field=models.TextField(default=0, verbose_name=15),
            preserve_default=False,
        ),
    ]