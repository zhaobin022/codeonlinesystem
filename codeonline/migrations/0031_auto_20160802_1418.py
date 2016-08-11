# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0030_onlinerequest_product_manager_confirm_before_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinerequest',
            name='product_confirm_after_online',
            field=models.ManyToManyField(related_name='product_confirm_after_online', verbose_name='\u4ea7\u54c1\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.RemoveField(
            model_name='onlinerequest',
            name='product_man_confirm_after_online',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='product_man_confirm_after_online',
            field=models.ForeignKey(related_name='product_man_confirm_after_online', verbose_name='\u4ea7\u54c1\u7ecf\u7406\u4e0a\u7ebf\u524d\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
