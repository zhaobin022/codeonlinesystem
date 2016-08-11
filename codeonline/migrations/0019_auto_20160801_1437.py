# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0018_auto_20160801_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='developer_fun_confirm_before_online',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='developer_fun_confirm_before_online',
            field=models.ManyToManyField(related_name='developer_fun_confirm_before_online', null=True, verbose_name='\u5f00\u53d1\u4eba\u5458\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
