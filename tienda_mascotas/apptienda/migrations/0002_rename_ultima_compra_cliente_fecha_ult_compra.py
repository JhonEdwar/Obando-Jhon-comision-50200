# Generated by Django 5.0.1 on 2024-02-27 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='ultima_compra',
            new_name='fecha_ult_compra',
        ),
    ]
