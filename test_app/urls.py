from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import contacts

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('contacts.urls')),
)

urlpatterns += staticfiles_urlpatterns()
