# Generated by Django 4.2.2 on 2023-06-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinosturisticos',
            name='imagenCiudad',
            field=models.ImageField(upload_to='imagenes/'),
        ),
    ]
