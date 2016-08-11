# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=64)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.CharField(max_length=20, verbose_name='\u9879\u76ee\u540d')),
                ('description', models.CharField(max_length=20, verbose_name='\u5e94\u7528\u63cf\u8ff0')),
            ],
        ),
        migrations.CreateModel(
            name='OnlineRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_time', models.DateTimeField(auto_now_add=True, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('function_type', models.IntegerField(blank=True, null=True, verbose_name='\u529f\u80fd\u7c7b\u578b', choices=[(1, b'app'), (2, b'bug'), (3, b'both')])),
                ('test_result_tag', models.BooleanField(default=False, verbose_name='\u6d4b\u8bd5\u7ed3\u679c')),
                ('version_tag', models.CharField(max_length=30, verbose_name='\u7248\u672c\u6807\u8bc6', blank=True)),
                ('online_function', models.TextField(verbose_name='\u4e0a\u7ebf\u529f\u80fd')),
                ('online_files', models.TextField(verbose_name='\u4e0a\u7ebf\u6587\u4ef6')),
                ('online_operation', models.IntegerField(blank=True, null=True, verbose_name='\u53d1\u7248\u662f\u5426\u9700\u8981\u5982\u4e0b\u64cd\u4f5c', choices=[(1, '\u91cd\u542f\u7f13\u5b58'), (2, '\u5b9a\u65f6\u4efb\u52a1')])),
                ('suggest_update_time', models.DateTimeField(null=True, verbose_name='\u5efa\u8bae\u4e0a\u7ebf\u65f6\u95f4', blank=True)),
                ('update_code_time', models.DateTimeField(null=True, verbose_name='\u4ee3\u7801\u4e0a\u7ebf\u65f6\u95f4', blank=True)),
                ('online_request_status', models.IntegerField(blank=True, null=True, verbose_name='\u6d41\u7a0b\u72b6\u6001', choices=[(1, '\u4ea7\u54c1\u7ecf\u7406\u5df2\u63d0\u4ea4\u7533\u8bf7'), (2, '\u4e0a\u7ebf\u524d\u5f00\u53d1\u7ec4\u957f\u5df2\u786e\u8ba4'), (3, '\u4e0a\u7ebf\u524d\u6d4b\u8bd5\u7ecf\u7406\u5df2\u786e\u8ba4'), (4, '\u4e0a\u7ebf\u524d\u6280\u672f\u7ecf\u7406\u5df2\u786e\u8ba4'), (5, '\u8fd0\u7ef4\u4e0a\u7ebf\u5df2\u786e\u8ba4'), (6, '\u8fd0\u7ef4\u7ecf\u7406\u4e0a\u7ebf\u5df2\u786e\u8ba4'), (7, '\u6d4b\u8bd5\u7ecf\u7406\u4e0a\u7ebf\u540e\u5df2\u786e\u8ba4'), (8, '\u4ea7\u54c1\u7ecf\u7406\u4e0a\u7ebf\u540e\u5df2\u786e\u8ba4(\u5b8c\u7ed3)')])),
                ('app', models.ManyToManyField(to='codeonline.App', verbose_name='\u4e0a\u7ebf\u9879\u76ee')),
                ('cto_confirm', models.ForeignKey(related_name='cto_confirm', verbose_name='CTO\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('developer', models.ManyToManyField(related_name='developer', verbose_name='\u5f00\u53d1\u4eba\u5458', to=settings.AUTH_USER_MODEL)),
                ('developer_fun_confirm_before_online', models.ForeignKey(related_name='developer_fun_confirm_before_online', verbose_name='\u5f00\u53d1\u4eba\u5458\u529f\u80fd\u786e\u8ba4', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('maintenance_manager_comfirm', models.ManyToManyField(related_name='maintenance_manager_comfirm', verbose_name='\u8fd0\u7ef4\u7ecf\u7406\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True)),
                ('maintenance_persion_comfirm', models.ManyToManyField(related_name='maintenance_persion_comfirm', verbose_name='\u8fd0\u7ef4\u4eba\u5458\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True)),
                ('product_man_confirm_after_online', models.ManyToManyField(related_name='product_man_confirm_after_online', verbose_name='\u4ea7\u54c1\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True)),
                ('product_man_confirm_before_online', models.ManyToManyField(related_name='product_man_confirm_before_online', verbose_name='\u4ea7\u54c1\u7ecf\u7406\u4e0a\u7ebf\u524d\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True)),
                ('require_side', models.ManyToManyField(related_name='require_side', verbose_name='\u9700\u6c42\u65b9', to=settings.AUTH_USER_MODEL)),
                ('technical_man_fun_confirm_online', models.ManyToManyField(related_name='technical_man_fun_confirm_online', verbose_name='\u6280\u672f\u7ecf\u7406\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True)),
                ('test_confirm_after_online', models.ManyToManyField(related_name='test_confirm_after_online', verbose_name='\u6d4b\u8bd5\u4eba\u5458\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True)),
                ('test_confirm_before_online', models.ManyToManyField(related_name='test_confirm_before_online', verbose_name='\u6d4b\u8bd5\u4eba\u5458\u4e0a\u7ebf\u524d\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True)),
                ('test_man_confirm_after_online', models.ManyToManyField(related_name='test_man_confirm_after_online', verbose_name='\u6d4b\u8bd5\u7ecf\u7406\u4e0a\u7ebf\u540e\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True)),
                ('white_box_test', models.ManyToManyField(related_name='white_box_test', verbose_name='\u767e\u76d2\u529f\u80fd\u786e\u8ba4', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=20, verbose_name='\u7ec4\u540d')),
                ('description', models.CharField(max_length=20, null=True, verbose_name='\u7ec4\u63cf\u8ff0', blank=True)),
            ],
        ),
    ]
