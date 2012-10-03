from django.contrib import admin, messages
from django.forms.widgets import Textarea
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
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'mac':
            kwargs['widget'] = Textarea
        return super(PCAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(PC, PCAdmin)
