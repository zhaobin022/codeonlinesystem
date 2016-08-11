# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0025_auto_20160802_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='maintenance_manager_comfirm',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='maintenance_manager_comfirm',
            field=models.ForeignKey(related_name='maintenance_manager_comfirm', verbose_name='\u8fd0\u7ef4\u7ecf\u7406\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='product_man_confirm_after_online',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='product_man_confirm_after_online',
            field=models.ForeignKey(related_name='product_man_confirm_after_online', verbose_name='\u4ea7\u54c1\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='test_man_confirm_after_online',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='test_man_confirm_after_online',
            field=models.ForeignKey(related_name='test_man_confirm_after_online', verbose_name='\u6d4b\u8bd5\u7ecf\u7406\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
