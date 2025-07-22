from django import forms

class DeviceIPForm(forms.Form):
    device_ip = forms.CharField(label='Device IP Address', max_length=15)
