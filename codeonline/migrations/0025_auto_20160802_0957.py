# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0024_auto_20160802_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onlinerequest',
            name='maintenance_persion_comfirm',
        ),
        migrations.AddField(
            model_name='onlinerequest',
            name='maintenance_person_comfirm',
            field=models.ForeignKey(related_name='maintenance_person_comfirm', verbose_name='\u8fd0\u7ef4\u4eba\u5458\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
