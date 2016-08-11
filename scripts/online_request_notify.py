# -*- coding: UTF-8 -*-

import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codeonlinesystem.settings")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    sys.path.append(BASE_DIR)
    import django
    django.setup()
    from codeonline import models
    import datetime
    from codeonlinesystem import settings
    from codeonline.utils import sendmail
    online_request_list = models.OnlineRequest.objects.filter(
        test_man_confirm_after_online_time__lte=datetime.datetime.now()-datetime.timedelta(days=settings.NOTIFY_DAYS),
        online_request_status=7,
    )
    print online_request_list
    for i in online_request_list:
        msg = u'''
        流程单已超期两天请确定流程单:
        流程单ID: {item_id}
        功能: {online_function}
        system_url:http://online.xegood.com/'''.format(item_id=i.id,online_function=i.online_function)
        to = i.product_manager_confirm_before_online.email
        subject = u'流程单超期 (id:%d)' % i.id
        print msg
        sendmail(to=to,subject=subject,msg=msg,settings=settings)