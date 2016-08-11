# -*- coding: UTF-8 -*-

import string
import smtplib
def sendmail(to=None,subject=None,msg=None,settings=None):


    try:
        BODY = string.join((
           "From: %s" % settings.EMAIL_CONFIG['from'],
           "To: %s" % to,
           "Subject: %s" % subject,
           "",
           msg),"\r\n").encode('utf-8')

        smtp = smtplib.SMTP()
        smtp.connect(settings.EMAIL_CONFIG['smtp_server'],settings.EMAIL_CONFIG['port'])
        smtp.login(settings.EMAIL_CONFIG['username'],settings.EMAIL_CONFIG['password'])
        smtp.sendmail( settings.EMAIL_CONFIG['from'],to,BODY)
        smtp.quit()
    except Exception as e:
        print 'Exception: ', e