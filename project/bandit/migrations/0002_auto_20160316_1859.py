# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bandit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=128)),
                ('alt', models.CharField(max_length=128)),
                ('profile', models.OneToOneField(to='bandit.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_date', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
                ('seen', models.BooleanField(default=b'false')),
                ('band', models.ForeignKey(to='bandit.Band')),
                ('event', models.ForeignKey(to='bandit.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='type',
            new_name='profile_type',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date'),
        ),
    ]
