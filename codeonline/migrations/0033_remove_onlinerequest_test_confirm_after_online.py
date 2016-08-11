# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0032_remove_onlinerequest_product_confirm_after_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='test_confirm_after_online',
        ),
    ]
