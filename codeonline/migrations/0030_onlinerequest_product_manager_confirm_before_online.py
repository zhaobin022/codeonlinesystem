# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0029_auto_20160802_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinerequest',
            name='product_manager_confirm_before_online',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1\u7ecf\u7406\u4e0a\u7ebf\u524d\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
