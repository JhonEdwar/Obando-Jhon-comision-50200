# Generated by Django 5.0.1 on 2024-03-04 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptienda', '0010_medicamento_tipo_de_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='tipo_de_animal',
            field=models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato')], max_length=20),
        ),
    ]