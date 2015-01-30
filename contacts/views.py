from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
import forms
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class ListContactView(LoggedInMixin, ListView):
    model = Contact
    template_name = 'contact_list.html'
    
    def get_queryset(self):
        contact_list = Contact.objects.filter(owner=self.request.user)
        
        paginator = Paginator(contact_list, 5)
        page = self.request.GET.get('page')
        
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        return contacts
        

class CreateContactView(LoggedInMixin, CreateView):
    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm
    
    def get_success_url(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return reverse('contacts-list')
        

class UpdateContactView(LoggedInMixin, UpdateView):
    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm
    
    def get_success_url(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit', kwargs={'pk': self.get_object().id})
        return reverse('contacts-list')


class DeleteContactView(LoggedInMixin, DeleteView):
    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')


class EditContactAddressView(LoggedInMixin, UpdateView):
    model = Contact
    template_name = 'edit_addresses.html'
    form_class = forms.ContactAddressFormSet

    def get_success_url(self):
        # redirect to the Contact view.
        return self.get_object().get_absolute_url()


class ContactView(LoggedInMixin, DetailView):
    model = Contact
    template_name = 'contact.html'

