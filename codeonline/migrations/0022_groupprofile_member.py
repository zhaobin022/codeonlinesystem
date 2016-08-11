# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0021_remove_onlinerequest_cto_confirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupprofile',
            name='member',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
