# Generated by Django 5.1.2 on 2024-10-11 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cargo_id_alter_cliente_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='escolaridade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.escolaridade'),
        ),
    ]
