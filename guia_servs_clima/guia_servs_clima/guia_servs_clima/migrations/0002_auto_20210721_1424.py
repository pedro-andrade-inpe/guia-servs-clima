# Generated by Django 3.1.7 on 2021-07-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_servs_clima', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacao',
            name='logo',
            field=models.ImageField(blank=True, upload_to='organizacao_logos', verbose_name='Logo'),
        ),
    ]