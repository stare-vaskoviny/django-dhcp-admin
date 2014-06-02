
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseServerError
import string

from .models import PC, NET_PART


class AddMacView(View):

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
                           ip='%s.%i' % (NET_PART, i))
                    p.save()
                    return HttpResponse('OK')
                except Exception:
                    pass
        return HttpResponseServerError('FULL')
