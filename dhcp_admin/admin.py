from django.contrib import admin

from .forms import MyPCAdminForm
from .models import PC
    
class PCAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip')
    search_fields = ['name', 'ip', 'mac']
    form = MyPCAdminForm

admin.site.register(PC, PCAdmin)
