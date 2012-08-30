'''
Created on Aug 30, 2012

@author: vencax
'''
import string

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from .models import PC

class MyPCAdminForm(forms.ModelForm):
    class Meta:
        model = PC
        
    def clean_mac(self):
        mac = self.cleaned_data['mac']
        cleaned = ''
        for l in mac:
            if l in string.hexdigits:
                cleaned += l
        if len(cleaned) != 12:
            raise ValidationError(_('incorect mac address'))
        return cleaned