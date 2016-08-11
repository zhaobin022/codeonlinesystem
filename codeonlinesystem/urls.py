"""codeonlinesystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from codeonline import views as codeonline_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',codeonline_view.index ),
    url(r'^online_request_list/$',codeonline_view.online_request_list,name='online_request_list'),
    url(r'^get_reqest_list_json_api/$',codeonline_view.get_reqest_list_json_api,name='get_reqest_list_json_api'),
    url(r'^update_request_api/$',codeonline_view.update_request_api,name='update_request_api'),
    url(r'^login/$',codeonline_view.login),
    url(r'^logout/$',codeonline_view.logout),
    url(r'^dashboard/$',codeonline_view.dashboard,name='dashboard'),
    url(r'^reset_password/$',codeonline_view.reset_password),
]
