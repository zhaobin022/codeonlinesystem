# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeonline', '0004_auto_20160801_1156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onlinerequest',
            options={'permissions': (('production_manaager_permission', 'production_manaager_permission'), ('develop_manager_permission', 'develop_manager_permission'), ('test_manaager_permission', 'test_manaager_permission'), ('maintenance_persion_permission', 'maintenance_persion_permission'), ('maintenance_manager_permission', 'maintenance_manager_permission'))},
        ),
    ]
