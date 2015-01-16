from django.conf.urls import patterns, include, url
from contacts.views import ListContactView, CreateContactView

urlpatterns = patterns('',
    url(r'^$', ListContactView.as_view(), name='contacts-list',),
    url(r'^new/', CreateContactView.as_view(), name='contacts-new',),
)