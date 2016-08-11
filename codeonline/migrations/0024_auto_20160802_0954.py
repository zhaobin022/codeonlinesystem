# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0023_onlinerequest_suggest_update_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='technical_man_fun_confirm_online',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='technical_man_fun_confirm_online',
            field=models.ForeignKey(related_name='technical_man_fun_confirm_online', verbose_name='\u6280\u672f\u7ecf\u7406\u529f\u80fd\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
