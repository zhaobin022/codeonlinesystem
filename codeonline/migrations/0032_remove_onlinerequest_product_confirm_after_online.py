# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0031_auto_20160802_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='product_confirm_after_online',
        ),
    ]
