# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('mirror.views',
    url(r'^showpics/$', 'showpics', name='showpics'),
    url(r'^review/$', 'review', name='review'),
)
