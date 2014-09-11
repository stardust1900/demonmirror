from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demon_mirror.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^band$', 'dmWeibo.views.band', name='band'),
    url(r'^call_back$', 'dmWeibo.views.call_back', name='call_back'),
    url(r'^cancel_auth$', 'dmWeibo.views.cancel_auth', name='cancel_auth'),
    url(r'^get_mentions$', 'dmWeibo.views.get_mentions', name='get_mentions'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mirror/', include('mirror.urls')),
)
