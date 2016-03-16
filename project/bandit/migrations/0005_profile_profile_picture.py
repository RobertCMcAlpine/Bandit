# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bandit.models


class Migration(migrations.Migration):

    dependencies = [
        ('bandit', '0004_auto_20160316_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=bandit.models.get_image_path, blank=True),
            preserve_default=True,
        ),
    ]
