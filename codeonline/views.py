# -*- coding: UTF-8 -*-
from django.contrib import auth
from django.contrib.auth import models as auth_models
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from permissions import _auth
import models
import json
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
import forms
from django.contrib.auth.decorators import login_required
import django.utils.timezone
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import resolve, reverse

# Create your views here.
# @_auth('aa')


@login_required
def index(request):
    return render(request, 'index.html', {})

@login_required
def online_request_list(request):
    if request.method == 'GET':
        online_request_status = request.GET.get('online_request_status',None)
        if online_request_status:
            request_list = models.OnlineRequest.objects.filter(online_request_status=int(online_request_status)).order_by('-id')
        else:
            request_list = models.OnlineRequest.objects.all().order_by('-id')
        # for l in request_list:
        #     l.developer.select_related().all()
        return render(request, 'online_request_list.html', {'request_list': request_list})

@login_required
@csrf_exempt
def get_reqest_list_json_api(request):
    if request.method == "GET":
        request_id = request.GET.get('id')
        try:
            request_item = models.OnlineRequest.objects.get(id=request_id)
            print request_item
        except Exception, e:
            print str(e)
            request_item = None
        ret = {}
        print request.GET
        if request_item:
            try:
                ret['status'] = True
                ret['msg'] = 'get result successfull !'

                # 初始化数据结构
                ret['data'] = {}
                online_request_status =  request_item.online_request_status
                ret['data']['online_request_status'] = online_request_status
            except Exception,e:
                print u'初始化数据结构'+str(e)

            try:
                # 填充申请时间

                ret['data']['request_time'] = (request_item.request_time + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

            except Exception,e:
                print u'填充申请时间'+str(e)

            try:
                # 填充开发人员
                ret['data']['developer'] = {}
                # ret['data']['developer']['all'] = {}
                ret['data']['developer']['selected'] = list(request_item.developer_confirm_before_online.select_related().values('id','alias'))

                if request_item.online_request_status == 1 and request.user.has_perm('codeonline.develop_manager_permission'):
                    developers = list(request.user.team_member.select_related().values('id','alias'))
                    ret['data']['developer']['edit'] = True
                else:
                    developers = ''

                ret['data']['developer']['all'] = developers
            except Exception,e:
                print u'填充开发人员'+str(e)

            try:
                # 填充需求方
                ret['data']['require_side'] = {}
                group = auth_models.Group.objects.get(name='production_manager')
                group_profile = group.groupprofile
                ret['data']['require_side']['all_product_manager'] = list(group_profile.member.select_related().values('id','alias'))
                ret['data']['require_side']['selected_product_manager'] = list(request_item.require_side.select_related().values('id','alias'))

            except Exception,e:
                print u'填充需求方'+str(e)


            try:
                # 测试结果
                if request_item.test_result_tag:
                    ret['data']['test_result_tag'] = True
                else:
                    ret['data']['test_result_tag'] = False

            except Exception,e:
                print u'测试结果'+str(e)
            # 建议上线时间suggest_update_time
            try:
                if request_item.suggest_update_time:
                    ret['data']['suggest_update_time'] = (
                        request_item.suggest_update_time + datetime.timedelta(hours=8)).strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    ret['data']['suggest_update_time'] = False
            except Exception,e:
                print u'建议上线时间suggest_update_time'+str(e)


            try:
                # 上线功能

                ret['data']['online_function'] = {}

                if request_item.online_request_status == 1 and request.user.has_perm('codeonline.develop_manager_permission'):
                    ret['data']['online_function']['edit'] = True
                if request_item.online_function:
                    ret['data']['online_function']['content'] = request_item.online_function
                else:
                    ret['data']['online_function']['content'] = False

            except Exception,e:
                print u'上线功能'+str(e)

            try:
                # 上线项目
                ret['data']['app'] = {}
                ret['data']['app']['all'] = list(models.App.objects.all().values('id','app_name'))
                ret['data']['app']['selected'] = list(request_item.app.select_related().values('id','app_name'))

                if request_item.online_request_status == 1 and request.user.has_perm('codeonline.develop_manager_permission'):
                    ret['data']['app']['edit'] = True
            except Exception,e:
                print u'上线项目'+str(e)

            try:
                # 上线文件

                ret['data']['online_files'] = {}

                if request_item.online_files:
                    ret['data']['online_files']['content'] = request_item.online_files
                else:
                    ret['data']['online_files']['content'] = False

                if request_item.online_request_status == 1 and request.user.has_perm('codeonline.develop_manager_permission'):
                    ret['data']['online_files']['edit'] = True

            except Exception,e:
                print u'上线文件'+str(e)
                # ret['data']['developer_fun_confirm_before_online'] = {}
                # if request_item.developer_fun_confirm_before_online:
                #     p = request_item.developer_fun_confirm_before_online
                #     ret['data']['developer_fun_confirm_before_online'][p.id] = p.username
            try:
                ret['data']['product_manager_confirm_before_online'] = {}
                if request_item.product_manager_confirm_before_online:
                    ret['data']['product_manager_confirm_before_online']['content'] = request_item.product_manager_confirm_before_online.alias
                else:
                    ret['data']['product_manager_confirm_before_online']['content'] = False

            except Exception,e:
                print u'product_manager_confirm_before_online'+str(e)

                # 产品经理上线前确认
            try:
                ret['data']['product_manager_confirm_before_online'] = {}
                if request_item.product_manager_confirm_before_online:
                    ret['data']['product_manager_confirm_before_online']['content'] = request_item.product_manager_confirm_before_online.alias
                else:
                    ret['data']['product_manager_confirm_before_online']['content'] = False
            except Exception,e:
                print u'product_manager_confirm_before_online'+str(e)

                # 上线前技术经理确认
            try:
                ret['data']['developer_man_confirm_before_online'] = {}
                if request_item.developer_man_confirm_before_online:
                    ret['data']['developer_man_confirm_before_online']['content'] = request_item.developer_man_confirm_before_online.alias
                else:
                    ret['data']['developer_man_confirm_before_online']['content'] = False
            except Exception,e:
                print u'developer_man_confirm_before_online'+str(e)

            try:

                ret['data']['test_confirm_before_online'] = {}
                ret['data']['test_confirm_before_online']['selected'] = list(request_item.test_confirm_before_online.select_related().values('id','alias'))

                if request_item.online_request_status == 2 and request.user.has_perm('codeonline.test_manager_permission'):
                    ret['data']['test_confirm_before_online']['all'] = list(request.user.team_member.select_related().values("id","alias"))
                    ret['data']['test_confirm_before_online']['edit'] = True
            except Exception,e:
                print u'test_confirm_before_online'+str(e)
                # 上线前技术经理确认
            try:
                ret['data']['technical_man_fun_confirm_online'] = {}
                if request_item.technical_man_fun_confirm_online:
                    ret['data']['technical_man_fun_confirm_online']['content'] = request_item.technical_man_fun_confirm_online.alias
                else:
                    ret['data']['technical_man_fun_confirm_online']['content'] = False
            except Exception,e:
                print u'technical_man_fun_confirm_online'+str(e)



            try:
                #运维上线确认
                ret['data']['maintenance_person_comfirm'] = {}
                if request_item.maintenance_person_comfirm:
                    ret['data']['maintenance_person_comfirm']['content'] = request_item.maintenance_person_comfirm.alias
                else:
                    ret['data']['maintenance_person_comfirm']['content'] = False
            except Exception,e:
                print u'maintenance_person_comfirm'+str(e)



            try:
                #测试经理上线前确认
                ret['data']['test_man_confirm_before_online'] = {}
                if request_item.test_man_confirm_before_online:
                    ret['data']['test_man_confirm_before_online']['content'] = request_item.test_man_confirm_before_online.alias
                else:
                    ret['data']['test_man_confirm_before_online']['content'] = False
            except Exception,e:
                print u'test_man_confirm_before_online'+str(e)


            try:

                #运维经理上线确认
                ret['data']['maintenance_manager_comfirm'] = {}
                if request_item.maintenance_manager_comfirm:
                    ret['data']['maintenance_manager_comfirm']['content'] = request_item.maintenance_manager_comfirm.alias
                else:
                    ret['data']['maintenance_manager_comfirm']['content'] = False
            except Exception,e:
                print u'maintenance_manager_comfirm'+str(e)

            try:
                #测试经理上线后确认

                ret['data']['test_man_confirm_after_online'] = {}
                if request_item.test_man_confirm_after_online:
                    ret['data']['test_man_confirm_after_online']['content'] = request_item.test_man_confirm_after_online.alias
                else:
                    ret['data']['test_man_confirm_after_online']['content'] = False
            except Exception,e:
                print u'test_man_confirm_after_online'+str(e)

            try:

                #产品经理上线后确认
                ret['data']['product_man_confirm_after_online'] = {}
                if request_item.product_man_confirm_after_online:
                    ret['data']['product_man_confirm_after_online']['content'] = request_item.product_man_confirm_after_online.alias
                else:
                    ret['data']['product_man_confirm_after_online']['content'] = False
            except Exception,e:
                print u'product_man_confirm_after_online'+str(e)


            if request_item.online_request_status == 1 and request.user.has_perm('codeonline.develop_manager_permission') or \
                request_item.online_request_status == 2 and request.user.has_perm('codeonline.test_manager_permission') or \
                request_item.online_request_status == 3 and request.user.has_perm('codeonline.technical_manager_permission') or \
                request_item.online_request_status == 4 and request.user.has_perm('codeonline.maintenance_person_permission') or \
                request_item.online_request_status == 5 and request.user.has_perm('codeonline.maintenance_manager_permission') or \
                request_item.online_request_status == 6 and request.user.has_perm('codeonline.test_manager_permission') or \
                request_item.online_request_status == 7 and request.user.has_perm('codeonline.production_manager_permission'):
                ret['data']['button_edit'] = True

        else:
            try:

                print 'request_item null.............'
                ret['status'] = True
                ret['msg'] = 'get result successfull !'
                # 初始化数据结构
                ret['data'] = {}

                # 填充需求方
                ret['data']['require_side'] = {}
                production_group = auth_models.Group.objects.get(name='production_manager')
                production_group_profile = production_group.groupprofile
                production_mans = production_group_profile.member.select_related().values('id','alias')
                ret['data']['require_side']= list(production_mans)
                print json.dumps(ret)

            except Exception,e:
                print str(e),'获取新上线单基础数据'
        print ret
        return HttpResponse(json.dumps(ret))

    else:
        return HttpResponse("ok")

@login_required
def update_request_api(request):
    if request.method == 'POST':
        online_request_status = request.POST.get("online_request_status", None)
        print request.POST

        if online_request_status == '0' and request.user.has_perm('codeonline.production_manager_permission') and not request.user.is_superuser:
            online_function = request.POST.get('online_function', None)
            require_side = request.POST.getlist('require_side_create', None)
            suggest_update_time = request.POST.get('suggest_update_time', None)
            submit_dic = {}

            if len(online_function) == 0 or len(require_side) == 0:
                return HttpResponseRedirect(reverse('online_request_list'))

            if suggest_update_time:
                suggest_update_time = datetime.datetime.strptime(suggest_update_time, "%Y-%m-%d %H:%M:%S")
                submit_dic['suggest_update_time'] = suggest_update_time

            if str(request.user.id) not in require_side:
                require_side.append(str(request.user.id))
            submit_dic['product_manager_confirm_before_online'] = request.user
            submit_dic['online_function'] = online_function
            submit_dic['online_request_status'] = 1

            online_request = models.OnlineRequest.objects.create(**submit_dic)
            for id in require_side:
                u = models.User.objects.get(id=id)
                online_request.require_side.add(u)

        elif online_request_status == '1' and request.user.has_perm('codeonline.develop_manager_permission') and not request.user.is_superuser:
            request_item_id = request.POST.get('request_item_id', None)
            developers = request.POST.getlist('developer', None)
            online_files = request.POST.get('online_files', None)
            app_ids = request.POST.getlist('app', None)
            online_request = models.OnlineRequest.objects.get(id=request_item_id)
            online_request.developer_man_confirm_before_online = request.user
            if online_files:
                if len(online_files) != 0:
                    online_request.online_files = online_files

            current_user_id = str(request.user.id)
            if not current_user_id in developers:
                developers.append(current_user_id)
            developer_set = models.User.objects.filter(id__in=developers)
            for l in developer_set:
                online_request.developer_confirm_before_online.add(l)

            app_set = models.App.objects.filter(id__in=app_ids)
            for a in app_set:
                online_request.app.add(a)
            online_request.online_request_status = 2
            online_request.developer_confirm_before_online_time = django.utils.timezone.now()
            online_request.save()

        elif online_request_status == '2' and request.user.has_perm('codeonline.test_manager_permission') and not request.user.is_superuser:
            request_item_id = request.POST.get('request_item_id', None)
            test_confirm_before_online = request.POST.getlist('test_confirm_before_online', None)
            request_item = models.OnlineRequest.objects.get(id=request_item_id)

            if str(request.user.id) not in test_confirm_before_online:
                test_confirm_before_online.append(str(request.user.id))
            if test_confirm_before_online:
                for p in test_confirm_before_online:
                    request_item.test_confirm_before_online.add(p)

            if request_item:
                request_item.online_request_status = 3
                request_item.test_result_tag = True
                request_item.test_man_confirm_before_online = request.user
                request_item.test_confirm_before_online_time = django.utils.timezone.now()
                request_item.save()
        elif online_request_status == '3' and request.user.has_perm('codeonline.technical_manager_permission') and not request.user.is_superuser:
            request_item_id = request.POST.get('request_item_id', None)
            if request_item_id:
                request_item = models.OnlineRequest.objects.get(id=request_item_id)
                request_item.online_request_status = 4
                request_item.technical_man_fun_confirm_online=request.user
                request_item.technical_man_fun_confirm_online_time = django.utils.timezone.now()
                request_item.save()

        elif online_request_status == '4' and request.user.has_perm('codeonline.maintenance_person_permission'):
            request_item_id = request.POST.get('request_item_id', None)
            if request_item_id:
                request_item = models.OnlineRequest.objects.get(id=request_item_id)
                request_item.online_request_status = 5
                request_item.update_code_time = django.utils.timezone.now()
                request_item.maintenance_person_comfirm=request.user
                request_item.save()
        elif online_request_status == '5' and request.user.has_perm('codeonline.maintenance_manager_permission'):
            request_item_id = request.POST.get('request_item_id', None)
            if request_item_id:
                request_item = models.OnlineRequest.objects.get(id=request_item_id)
                request_item.online_request_status = 6
                request_item.maintenance_manager_comfirm=request.user
                request_item.maintenance_manager_comfirm_time = django.utils.timezone.now()
                request_item.save()
        elif online_request_status == '6' and request.user.has_perm('codeonline.test_manager_permission') and not request.user.is_superuser:
            request_item_id = request.POST.get('request_item_id', None)
            if request_item_id:
                request_item = models.OnlineRequest.objects.get(id=request_item_id)
                request_item.online_request_status = 7
                request_item.test_man_confirm_after_online = request.user
                request_item.test_man_confirm_after_online_time = django.utils.timezone.now()
                request_item.save()

            else:
                return HttpResponse.HttpResponseForbidden
        elif online_request_status == '7' and request.user.has_perm('codeonline.production_manager_permission') and not request.user.is_superuser:
            request_item_id = request.POST.get('request_item_id', None)
            if request_item_id:
                request_item = models.OnlineRequest.objects.get(id=request_item_id)
                request_item.online_request_status = 8
                request_item.product_man_confirm_after_online = request.user
                request_item.product_man_confirm_after_online_time = django.utils.timezone.now()
                request_item.save()
        return HttpResponseRedirect(reverse(online_request_list))
    else:
        return HttpResponse('create requeset fail')

def login(request):
    if request.method == 'GET':
        form = forms.UserLoginForm()
        return render(request, 'login.html', {'form':form})
    else:
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            user_login_form_info = form.clean()
            username = user_login_form_info['username']
            password = user_login_form_info['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')

            else:
                print 'login fail'
                errors = {}
                errors['login'] = [u'用户名或密码错误']

                return render(request, 'login.html', {'form':form,'errors':errors})
        else:
            errors = form.errors
            return render(request, 'login.html', {'form':form,'errors':errors})
@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

@login_required
def dashboard(request):
    if request.method == 'GET':
        ret = {}

        for i in range(1,9):
            tag_name = 'step_%d' % i
            ret[tag_name]={}
            ret[tag_name]['online_request_status'] = i
            ret[tag_name]['count'] = models.OnlineRequest.objects.filter(online_request_status=i).count()
        return render(request, 'dashboard.html', {"ret":ret})


@login_required
def reset_password(request):
    if request.method == 'GET':
        form = forms.RestPassword()
        return render(request, 'reset_password.html', {'form':form})
    else:
        form = forms.RestPassword(request.POST)
        if form.is_valid():
            user_login_form_info = form.clean()
            repassword = user_login_form_info['repassword']
            password = user_login_form_info['password']
            oldpassword = user_login_form_info['oldpassword']
            user = auth.authenticate(username=request.user.username, password=oldpassword)
            errors = {}
            if user is not None and user.is_active:
                if password.strip() == repassword.strip():
                    user = request.user
                    user.set_password(password)
                    user.save()
                    auth.logout(request)
                    errors['successfull'] = [u'<a href="/login/">修改密码成功,请重新登录</a>']
                else:
                    errors['login'] = [u'新密码不一致']

            else:
                errors['login'] = [u'旧密码输入错误']

            return render(request, 'reset_password.html', {'form':form,'errors':errors})
        else:
            errors = form.errors
            return render(request, 'reset_password.html', {'form':form,'errors':errors})
