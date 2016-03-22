# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bandit.models


class Migration(migrations.Migration):

    dependencies = [
        ('bandit', '0009_event_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default=b'project/static/imges/defaultvenue.jpg', null=True, upload_to=bandit.models.get_image_path, blank=True),
        ),
    ]
