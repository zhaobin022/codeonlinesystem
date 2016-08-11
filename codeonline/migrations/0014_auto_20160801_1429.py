# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0013_auto_20160801_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='product_man_confirm_before_online',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='product_man_confirm_before_online_time',
        ),
    ]
