# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0015_auto_20160801_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='test_confirm_after_online',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='test_confirm_after_online_time',
        ),
    ]
