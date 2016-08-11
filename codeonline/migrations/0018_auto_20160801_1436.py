# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0017_onlinerequest_test_confirm_after_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='developer',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='request_time',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='suggest_update_time',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='test_confirm_after_online',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='product_man_confirm_before_online',
            field=models.ManyToManyField(related_name='product_man_confirm_before_online', verbose_name='\u4ea7\u54c1\u7ecf\u7406\u4e0a\u7ebf\u524d\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='product_man_confirm_before_online_time',
            field=models.DateTimeField(null=True, verbose_name='\u4ea7\u54c1\u7ecf\u7406\u4e0a\u7ebf\u524d\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='onlinerequest',
            name='maintenance_manager_comfirm_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u8fd0\u7ef4\u7ecf\u7406\u786e\u8ba4\u65f6\u95f4', null=True),
        ),
    ]
