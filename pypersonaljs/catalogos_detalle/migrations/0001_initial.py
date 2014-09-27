# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion1', models.CharField(max_length=255)),
                ('descripcion2', models.CharField(max_length=255)),
                ('monto1', models.DecimalField(max_digits=18, decimal_places=2)),
                ('monto2', models.DecimalField(max_digits=18, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
