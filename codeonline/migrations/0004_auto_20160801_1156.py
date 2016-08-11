# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0003_auto_20160801_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=20, null=True, verbose_name='\u4eba\u5458\u63cf\u8ff0', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='group_admin_tag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='team_member',
            field=models.ManyToManyField(related_name='team_leader_set', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
