from django.shortcuts import render
from .utils import DNAC_Manager
from .forms import DeviceIPForm

dnac = DNAC_Manager()

def menu(request):
    return render(request, 'dna_center_cisco/menu.html')

def auth_token(request):
    dnac.get_auth_token()
    return render(request, 'dna_center_cisco/token.html', {'token': dnac.token})

def list_devices(request):
    devices = dnac.get_network_devices()
    return render(request, 'dna_center_cisco/devices.html', {'devices': devices})

def device_interfaces(request):
    interfaces = None
    if request.method == "POST":
        form = DeviceIPForm(request.POST)
        if form.is_valid():
            ip = form.cleaned_data['device_ip']
            interfaces = dnac.get_device_interfaces(ip)
    else:
        form = DeviceIPForm()
    return render(request, 'dna_center_cisco/interfaces.html', {
        'form': form, 
        'interfaces': interfaces
    })
