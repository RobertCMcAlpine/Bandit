# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandit', '0002_auto_20160316_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='band',
            field=models.ForeignKey(blank=True, to='bandit.Band', null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
