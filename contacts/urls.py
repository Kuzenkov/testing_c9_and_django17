from django.conf.urls import patterns, include, url
from contacts.views import ListContactView, CreateContactView, EditContactAddressView
from contacts.views import DeleteContactView, UpdateContactView, ContactView

urlpatterns = patterns('',
    url(r'^$', ListContactView.as_view(), name='contacts-list',),
    url(r'^new/$', CreateContactView.as_view(), name='contacts-new',),
    url(r'^edit/(?P<pk>\d+)/$', UpdateContactView.as_view(), name='contacts-edit',),
    url(r'^delete/(?P<pk>\d+)/$', DeleteContactView.as_view(), name='contacts-delete',),
    url(r'^(?P<pk>\d+)/$', ContactView.as_view(), name='contacts-view',),
    url(r'^edit/(?P<pk>\d+)/addresses/$', EditContactAddressView.as_view(),
        name='contacts-edit-addresses',),
)