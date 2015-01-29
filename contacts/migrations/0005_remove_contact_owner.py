# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20150122_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='owner',
        ),
    ]
