# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0022_groupprofile_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinerequest',
            name='suggest_update_time',
            field=models.DateTimeField(null=True, verbose_name='\u5efa\u8bae\u4e0a\u7ebf\u65f6\u95f4', blank=True),
        ),
    ]
