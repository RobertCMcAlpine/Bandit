# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_members', models.PositiveIntegerField()),
                ('genre', models.CharField(max_length=128, choices=[(b'Alternative', b'Alternative'), (b'Blues/R&B', b'Blues/R&B'), (b'Childrens Music', b'Childrens Music'), (b'Classical', b'Classical'), (b'Country', b'Country'), (b'Dance', b'Dance'), (b'Easy Listening', b'Easy Listening'), (b'Electronic', b'Electronic'), (b'Folk', b'Folk'), (b'House', b'House'), (b'Industrial', b'Industrial'), (b'Techno', b'Techno'), (b'Trance', b'Trance'), (b'Hip Hop/Rap', b'Hip Hop/Rap'), (b'Holiday', b'Holiday'), (b'Jazz', b'Jazz'), (b'New Age', b'New Age'), (b'Pop', b'Pop'), (b'Religious', b'Religious'), (b'Rock', b'Rock'), (b'Soundtrack', b'Soundtrack'), (b'Unclassifiable', b'Unclassifiable'), (b'World', b'World')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('reward', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=1024)),
                ('band', models.ForeignKey(to='bandit.Band')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('type', models.CharField(max_length=1, choices=[(b'B', b'Band'), (b'V', b'Venue')])),
                ('website', models.URLField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=512)),
                ('post_code', models.CharField(max_length=10)),
                ('profile', models.OneToOneField(to='bandit.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(to='bandit.Venue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='band',
            name='profile',
            field=models.OneToOneField(to='bandit.Profile'),
            preserve_default=True,
        ),
    ]
