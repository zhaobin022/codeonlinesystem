# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0016_auto_20160801_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinerequest',
            name='test_confirm_after_online',
            field=models.ManyToManyField(related_name='test_confirm_after_online', verbose_name='\u6d4b\u8bd5\u4eba\u5458\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
