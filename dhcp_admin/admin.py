from django.contrib import admin, messages
from django.utils.translation import ugettext_lazy as _

from .forms import MyPCAdminForm
from .models import PC


def start_pcs(modeladmin, request, queryset):
    for m in queryset:
        m.start()
    messages.add_message(request, messages.INFO, _('Wakeup signals sent.'))
start_pcs.short_description = _('Start selected machines')
    
class PCAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip')
    search_fields = ['name', 'ip', 'mac']
    form = MyPCAdminForm
    actions = [start_pcs]

admin.site.register(PC, PCAdmin)
