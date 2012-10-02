
from django.views.generic.base import View
from django.conf import settings
from django.http import HttpResponse, HttpResponseServerError
import string

from .models import PC

class AddMacView(View):
    
    net_part = getattr(settings, 'NET_PART', '10.0.0')
    
    def get(self, request, *args, **kwargs):
        mac, name = kwargs['mac'], kwargs['name'].lower()
        cleaned = ''
        for l in mac:
            if l in string.hexdigits:
                cleaned += l
        if not PC.objects.filter(mac=mac).exists():
            for i in range(10, 249):
                try:
                    p = PC(name=name, mac=cleaned, 
                           ip='%s.%i' % (self.net_part, i))
                    p.save()
                    return HttpResponse('OK')
                except Exception:
                    pass
        return HttpResponseServerError('FULL')
        