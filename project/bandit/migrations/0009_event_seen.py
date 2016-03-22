# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandit', '0008_auto_20160321_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='seen',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
