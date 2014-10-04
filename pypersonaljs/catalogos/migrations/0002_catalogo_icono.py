# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogo',
            name='icono',
            field=models.FileField(default='', upload_to=b'catalogos'),
            preserve_default=False,
        ),
    ]
