# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0014_auto_20160801_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinerequest',
            name='maintenance_manager_comfirm_time',
            field=models.DateTimeField(null=True, verbose_name='\u8fd0\u7ef4\u7ecf\u7406\u786e\u8ba4\u65f6\u95f4', blank=True),
        ),
    ]
