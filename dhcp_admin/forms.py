'''
Created on Aug 30, 2012

@author: vencax
'''
import re
import string

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.forms.widgets import Textarea

from .models import PC

mac_re = re.compile(r'([0-9A-Fa-f]{2}[:-]?){5}([0-9A-Fa-f]{2})')


class MyPCAdminForm(forms.ModelForm):

    class Meta:
        model = PC

    mac = forms.CharField(widget=Textarea)

    def clean_mac(self):
        mac = self.cleaned_data['mac']
        if not mac_re.search(mac):
            raise ValidationError(_('incorect mac address'))

        cleaned = ''
        for l in mac:
            if l in string.hexdigits:
                cleaned += l

        return cleaned
