# Generated by Django 5.1.1 on 2024-10-02 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0012_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='direccion',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='biblioteca.direccion'),
        ),
    ]
