# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0027_onlinerequest_request_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinerequest',
            name='request_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8d77\u7533\u8bf7\u65f6\u95f4', null=True),
        ),
    ]
