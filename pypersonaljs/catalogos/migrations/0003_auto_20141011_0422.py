# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0002_catalogo_icono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo',
            name='icono',
            field=models.ImageField(upload_to=b'catalogos'),
        ),
    ]
