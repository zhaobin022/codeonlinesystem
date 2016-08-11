#-*- coding: UTF-8 -*-
from django.db import models
from user_auth import User
from django.contrib.auth.models import Group



class GroupProfile(models.Model):
    group = models.OneToOneField(Group,blank=True)
    group_name = models.CharField(max_length=20, verbose_name=u'组名')
    description = models.CharField(max_length=20, blank=True,null=True,verbose_name=u'组描述')
    member = models.ManyToManyField(User,blank=True)
    def __unicode__(self):
        return self.group_name+self.description


class App(models.Model):
    app_name =  models.CharField(max_length=20, verbose_name=u'项目名')
    description = models.CharField(max_length=20, verbose_name=u'应用描述')
    def __unicode__(self):
        return self.app_name+self.description
class OnlineRequest(models.Model):
    online_function = models.TextField(verbose_name=u'上线功能')
    suggest_update_time = models.DateTimeField(verbose_name=u'建议上线时间',blank=True,null=True)
    request_time = models.DateTimeField(verbose_name=u'发起申请时间',blank=True,null=True,auto_now_add=True)

    require_side = models.ManyToManyField(User,verbose_name=u'需求方',related_name='require_side')

    product_manager_confirm_before_online = models.ForeignKey(User,blank=True,null=True,verbose_name=u'产品经理上线前确认')
    test_result_tag = models.BooleanField(default=False,verbose_name=u'测试结果')

    app = models.ManyToManyField(App,verbose_name=u'上线项目')
    online_files = models.TextField(verbose_name=u'上线文件')


    developer_confirm_before_online = models.ManyToManyField(User,blank=True,verbose_name=u'开发人员功能确认',related_name='developer_confirm_before_online')
    developer_man_confirm_before_online = models.ForeignKey(User,blank=True,null=True,verbose_name=u'开发经理功能确认',related_name='developer_man_confirm_before_online')
    developer_confirm_before_online_time = models.DateTimeField(verbose_name=u'开发经理功能确认时间',blank=True,null=True)

    test_confirm_before_online = models.ManyToManyField(User,blank=True,verbose_name=u'测试人员上线前功能确认',related_name='test_confirm_before_online')
    test_man_confirm_before_online = models.ForeignKey(User,blank=True,null=True,verbose_name=u'测试经理上线前功能确认',related_name='test_man_confirm_before_online')
    test_confirm_before_online_time = models.DateTimeField(verbose_name=u'测试人员上线前功能确认时间',blank=True,null=True)

    technical_man_fun_confirm_online = models.ForeignKey(User,blank=True,null=True,verbose_name=u'技术经理功能确认',related_name='technical_man_fun_confirm_online')
    technical_man_fun_confirm_online_time = models.DateTimeField(verbose_name=u'技术经理功能确认时间',blank=True,null=True)

    maintenance_person_comfirm = models.ForeignKey(User,blank=True,null=True,verbose_name=u'运维人员确认',related_name='maintenance_person_comfirm')
    update_code_time = models.DateTimeField(blank=True,null=True,verbose_name=u'代码上线时间')

    maintenance_manager_comfirm = models.ForeignKey(User,blank=True,null=True,verbose_name=u'运维经理确认',related_name='maintenance_manager_comfirm')
    maintenance_manager_comfirm_time = models.DateTimeField(blank=True,null=True,verbose_name=u'运维经理确认时间')


    test_man_confirm_after_online = models.ForeignKey(User,blank=True,null=True,verbose_name=u'测试经理上线后功能确认',related_name='test_man_confirm_after_online')
    test_man_confirm_after_online_time = models.DateTimeField(verbose_name=u'测试经理上线后功能确认时间',blank=True,null=True)

    product_man_confirm_after_online = models.ForeignKey(User,blank=True,null=True,verbose_name=u'产品经理上线后确认',related_name='product_man_confirm_after_online')
    product_man_confirm_after_online_time = models.DateTimeField(verbose_name=u'产品上线后功能确认时间',blank=True,null=True)



    online_request_status_choice = (
        (1,u'产品经理已提交申请'),
        (2,u'上线前开发组长已确认'),
        (3,u'上线前测试经理已确认'),
        (4,u'上线前技术经理已确认'),
        (5,u'运维上线已确认'),
        (6,u'运维经理上线已确认'),
        (7,u'测试经理上线后已确认'),
        (8,u'产品经理上线后已确认(完结)'),
    )
    online_request_status = models.IntegerField(blank=True,null=True,choices=online_request_status_choice,verbose_name=u'流程状态')

    def __unicode__(self):
        return str(self.id)+":"+self.online_function

    class Meta:
        permissions =(
                      ('production_manager_permission', u"production_manager_permission"),
                      ('develop_manager_permission',u"develop_manager_permission"),
                      ('test_manager_permission',u"test_manager_permission"),
                      ('maintenance_person_permission',u"maintenance_person_permission"),
                      ('maintenance_manager_permission',u"maintenance_manager_permission"),
                      ('technical_manager_permission',u"technical_manager_permission"),
                  )


