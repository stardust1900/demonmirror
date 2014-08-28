from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demon_mirror.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^band$', 'weibo.views.band', name='band'),
    url(r'^call_back$', 'weibo.views.call_back', name='call_back'),
    url(r'^cancel_auth$', 'weibo.views.cancel_auth', name='cancel_auth'),
    url(r'^admin/', include(admin.site.urls)),
)
