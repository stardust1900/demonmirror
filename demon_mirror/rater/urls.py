# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('rater.views',
    url(r'^test/$', 'test', name='test'),
)