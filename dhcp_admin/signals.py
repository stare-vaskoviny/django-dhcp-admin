
from command_runner import runCommand
            
def pcPostSaved(sender, instance, created, **kwargs):
    formattedMAC = []
    for i in range(0, len(instance.mac), 2):
        formattedMAC.append(instance.mac[i:i+2])
    runCommand('dhcpdManager.py del %s && dhcpdManager.py add %s %s %s' %\
                (instance.name, instance.name, 
                 ':'.join(formattedMAC), instance.ip))
    return instance
            
def pcPreDelete(sender, instance, **kwargs):
    runCommand('dhcpdManager.py del %s' % instance.name)
    return instance