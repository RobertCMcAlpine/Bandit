# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandit', '0007_auto_20160318_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(blank=True, max_length=128, null=True, choices=[(b'Alternative', b'Alternative'), (b'Blues/R&B', b'Blues/R&B'), (b'Childrens Music', b'Childrens Music'), (b'Classical', b'Classical'), (b'Country', b'Country'), (b'Dance', b'Dance'), (b'Easy Listening', b'Easy Listening'), (b'Electronic', b'Electronic'), (b'Folk', b'Folk'), (b'House', b'House'), (b'Industrial', b'Industrial'), (b'Techno', b'Techno'), (b'Trance', b'Trance'), (b'Hip Hop/Rap', b'Hip Hop/Rap'), (b'Holiday', b'Holiday'), (b'Jazz', b'Jazz'), (b'New Age', b'New Age'), (b'Pop', b'Pop'), (b'Religious', b'Religious'), (b'Rock', b'Rock'), (b'Soundtrack', b'Soundtrack'), (b'Unclassifiable', b'Unclassifiable'), (b'World', b'World')]),
        ),
        migrations.AlterField(
            model_name='band',
            name='number_of_members',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='reward',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='venue',
            name='address',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='post_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
