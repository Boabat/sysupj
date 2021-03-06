from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sysupj import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sysupj.views.home', name='home'),
    # url(r'^sysupj/', include('sysupj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	#url('^hello/$', views.hello),
	# url('^$', ua_display_good1),
	url('^$', views.home),
	url('^addComment/$', views.addComment),
	url('^register/$', views.register),
	url('^login/$', views.login),
	url('^logout/$', views.logout),
	url('^profile/$', views.profile),
    url('^upload/$', views.upload),
)