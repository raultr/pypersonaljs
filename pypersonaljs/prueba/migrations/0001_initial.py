# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoPrueba',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True)),
                ('clave', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('icono', models.FileField(upload_to=b'catalogos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
