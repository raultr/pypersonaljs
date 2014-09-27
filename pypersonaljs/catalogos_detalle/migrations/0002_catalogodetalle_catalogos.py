# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
        ('catalogos_detalle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogodetalle',
            name='catalogos',
            field=models.ForeignKey(default=1, to='catalogos.Catalogo'),
            preserve_default=True,
        ),
    ]
