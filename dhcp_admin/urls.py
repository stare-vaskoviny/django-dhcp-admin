from django.conf.urls.defaults import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^(?P<mac>[-:\w]+)/(?P<name>\w+)/$', views.AddMacView.as_view(),
        name='dhcp_admin_add_mac'),
)
