# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('codeonline', '0002_auto_20160801_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=20, verbose_name='\u7ec4\u540d')),
                ('description', models.CharField(max_length=20, null=True, verbose_name='\u7ec4\u63cf\u8ff0', blank=True)),
                ('group', models.OneToOneField(blank=True, to='auth.Group')),
            ],
        ),
        migrations.DeleteModel(
            name='UserGroups',
        ),
    ]
