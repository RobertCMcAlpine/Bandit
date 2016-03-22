# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bandit.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bandit', '0012_auto_20160322_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default=b'images/defaultvenue.jpg', null=True, upload_to=bandit.models.get_image_path, blank=True),
        ),
    ]
