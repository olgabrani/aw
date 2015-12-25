# -*- coding: utf-8 -*-
from  django import forms
from django.utils.translation import ugettext_lazy as _

class MyContactForm(forms.Form):
    name = forms.CharField(label=u'όνομα',error_messages={'required': u'Παρακαλώ συμπληρώστε το όνομα σας'})
    email = forms.EmailField(label='email',
    error_messages={
        'required': u'Παρακαλώ συμπληρώστε το email σας',
        'invalid': u'Το email που εισάγατε δεν είναι έγκυρο'
    })
    form_content = forms.CharField(widget=forms.Textarea,
        label=u'μήνυμα',error_messages={
                'required': u'Παρακαλώ συμπληρώστε το μήνυμα σας'
        })
