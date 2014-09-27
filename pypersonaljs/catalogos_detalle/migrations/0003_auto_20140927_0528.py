# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0002_catalogodetalle_catalogos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogodetalle',
            name='descripcion2',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='catalogodetalle',
            name='monto1',
            field=models.DecimalField(default=Decimal('0.00'), max_digits=18, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='catalogodetalle',
            name='monto2',
            field=models.DecimalField(default=Decimal('0.00'), max_digits=18, decimal_places=2),
        ),
    ]
