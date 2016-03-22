# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bandit.models


class Migration(migrations.Migration):

    dependencies = [
        ('bandit', '0010_auto_20160322_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default=b'static/imges/defaultvenue.jpg', null=True, upload_to=bandit.models.get_image_path, blank=True),
        ),
    ]
