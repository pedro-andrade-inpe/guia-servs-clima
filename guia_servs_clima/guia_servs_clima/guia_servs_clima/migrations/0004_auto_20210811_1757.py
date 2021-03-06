# Generated by Django 3.1.7 on 2021-08-11 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia_servs_clima', '0003_delete_organizacaositemap'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pagamento', models.CharField(max_length=100, verbose_name='Nome do Tipo de Pagamento')),
            ],
            options={
                'verbose_name': 'Tipo Pagamento',
                'verbose_name_plural': 'Tipos Pagamentos',
            },
        ),
        migrations.CreateModel(
            name='OrganizacaoTipoPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia_servs_clima.organizacao')),
                ('tipo_pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia_servs_clima.tipopagamento')),
            ],
            options={
                'unique_together': {('tipo_pagamento', 'organizacao')},
            },
        ),
        migrations.AddField(
            model_name='organizacao',
            name='tipos_pagamento',
            field=models.ManyToManyField(blank=True, through='guia_servs_clima.OrganizacaoTipoPagamento', to='guia_servs_clima.TipoPagamento'),
        ),
    ]
