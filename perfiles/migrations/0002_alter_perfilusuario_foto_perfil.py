# Generated by Django 5.1.1 on 2024-10-11 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='foto_perfil',
            field=models.ImageField(upload_to='fotos_perfil'),
        ),
    ]
