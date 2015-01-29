# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.contrib.auth.models import User

class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(default='1', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
