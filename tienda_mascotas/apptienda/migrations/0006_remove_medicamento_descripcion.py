# Generated by Django 5.0.1 on 2024-03-02 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptienda', '0005_remove_medicamento_tipo_de_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='descripcion',
        ),
    ]
