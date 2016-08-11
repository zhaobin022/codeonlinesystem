# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0012_auto_20160801_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinerequest',
            name='developer_fun_confirm_before_online_time',
            field=models.DateTimeField(null=True, verbose_name='\u5f00\u53d1\u4eba\u5458\u529f\u80fd\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='maintenance_manager_comfirm_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u8fd0\u7ef4\u7ecf\u7406\u786e\u8ba4\u65f6\u95f4', null=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='product_man_confirm_after_online_time',
            field=models.DateTimeField(null=True, verbose_name='\u4ea7\u54c1\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='product_man_confirm_before_online_time',
            field=models.DateTimeField(null=True, verbose_name='\u4ea7\u54c1\u7ecf\u7406\u4e0a\u7ebf\u524d\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='technical_man_fun_confirm_online_time',
            field=models.DateTimeField(null=True, verbose_name='\u6280\u672f\u7ecf\u7406\u529f\u80fd\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='test_confirm_after_online_time',
            field=models.DateTimeField(null=True, verbose_name='\u6d4b\u8bd5\u4eba\u5458\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='test_confirm_before_online_time',
            field=models.DateTimeField(null=True, verbose_name='\u6d4b\u8bd5\u4eba\u5458\u4e0a\u7ebf\u524d\u529f\u80fd\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='test_man_confirm_after_online_time',
            field=models.DateTimeField(null=True, verbose_name='\u6d4b\u8bd5\u7ecf\u7406\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
    ]
