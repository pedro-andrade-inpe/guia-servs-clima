from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('guia_servs_clima', '0006_auto_20210913_1539'),
    ]

    operations = [
        migrations.RunSQL(
            sql='CREATE EXTENSION IF NOT EXISTS unaccent;'
        )
    ]
