# Generated by Django 3.1.7 on 2021-10-06 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guia_servs_clima', '0011_auto_20211006_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizacao',
            old_name='updated_at',
            new_name='atualizado_em',
        ),
        migrations.RenameField(
            model_name='organizacao',
            old_name='created_at',
            new_name='criado_em',
        ),
    ]
