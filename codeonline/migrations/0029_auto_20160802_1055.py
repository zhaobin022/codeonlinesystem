# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0028_auto_20160802_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='developer_fun_confirm_before_online',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='developer_fun_confirm_before_online_time',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='function_type',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='online_operation',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='product_man_confirm_before_online',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='product_man_confirm_before_online_time',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='version_tag',
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='white_box_test',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='developer_confirm_before_online',
            field=models.ManyToManyField(related_name='developer_confirm_before_online', verbose_name='\u5f00\u53d1\u4eba\u5458\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='developer_confirm_before_online_time',
            field=models.DateTimeField(null=True, verbose_name='\u5f00\u53d1\u7ecf\u7406\u529f\u80fd\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='developer_man_confirm_before_online',
            field=models.ForeignKey(related_name='developer_man_confirm_before_online', verbose_name='\u5f00\u53d1\u7ecf\u7406\u529f\u80fd\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='test_confirm_after_online',
            field=models.ManyToManyField(related_name='test_confirm_after_online', verbose_name='\u6d4b\u8bd5\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='test_man_confirm_before_online',
            field=models.ForeignKey(related_name='test_man_confirm_before_online', verbose_name='\u6d4b\u8bd5\u7ecf\u7406\u4e0a\u7ebf\u524d\u529f\u80fd\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='onlinerequest',
            name='maintenance_manager_comfirm_time',
            field=models.DateTimeField(null=True, verbose_name='\u8fd0\u7ef4\u7ecf\u7406\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='product_man_confirm_after_online',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='product_man_confirm_after_online',
            field=models.ManyToManyField(related_name='product_man_confirm_after_online', verbose_name='\u4ea7\u54c1\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
