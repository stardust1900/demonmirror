from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demonmirror.views.home', name='home'),
    # url(r'^demonmirror/', include('demonmirror.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^band$', 'dmWeibo.views.band', name='band'),
    url(r'^call_back$', 'dmWeibo.views.call_back', name='call_back'),
    url(r'^cancel_auth$', 'dmWeibo.views.cancel_auth', name='cancel_auth'),
    url(r'^get_mentions$', 'dmWeibo.views.get_mentions', name='get_mentions'),
    url(r'^test','dmWeibo.views.test',name='test'),
    url(r'^mirror/', include('mirror.urls')),
    url(r'^rater/', include('rater.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^$', RedirectView.as_view(url='/mirror/showpics/')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)