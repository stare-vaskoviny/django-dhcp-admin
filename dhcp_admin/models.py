from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, pre_delete
from django.conf import settings
from command_runner import runCommand

from .signals import pcPostSaved, pcPreDelete

NET_PART = getattr(settings, 'NET_PART', '10.0.0')


class PC(models.Model):
    """ Represents PC in DHCP database. """
    class Meta:
        verbose_name = _('pc')
        verbose_name_plural = _('pcs')

    mac = models.CharField(verbose_name=_('macAddress'), max_length=12,
                           unique=True, primary_key=True)
    name = models.CharField(verbose_name=_('name'), max_length=64, unique=True)
    ip = models.IPAddressField(verbose_name=_('ip address'), unique=True)

    def status(self):
        return runCommand('ping -c 1 -W 1 %s' % self.ip) == 0

    def start(self):
        runCommand('wakeonlan -i %s.255 %s' % (NET_PART, self.formattedMAC()))

    def formattedMAC(self):
        formattedMAC = []
        for i in range(0, len(self.mac), 2):
            formattedMAC.append(self.mac[i:i + 2].lower())
        return ':'.join(formattedMAC)

    def stop(self):
        runCommand()

    def __unicode__(self):
        return 'PC %s' % self.name

post_save.connect(pcPostSaved, sender=PC, dispatch_uid='pc_post_save')
pre_delete.connect(pcPreDelete, sender=PC, dispatch_uid='pc_pre_delete')
