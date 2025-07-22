import requests
from requests.auth import HTTPBasicAuth
import urllib3
from datetime import datetime
from .dnac_config import DNAC
from .models import APILog

urllib3.disable_warnings()

class DNAC_Manager:
    def __init__(self):
        self.token = None

    def log_api_result(self, api_type, device_ip, success):
        try:
            APILog.objects.create(
                api_type=api_type,
                device_ip=device_ip,
                result='success' if success else 'failure',
            )
        except Exception as e:
            print(f"⚠️ Failed to log API result: {str(e)}")

    def get_auth_token(self, display_token=False):
        try:
            url = f"https://{DNAC['host']}:{DNAC['port']}/dna/system/api/v1/auth/token"
            response = requests.post(
                url,
                auth=HTTPBasicAuth(DNAC['username'], DNAC['password']),
                verify=False,
                timeout=10
            )
            response.raise_for_status()
            self.token = response.json()['Token']
            self.log_api_result("get_auth_token", None, True)
            return True
        except Exception as e:
            print(f"❌ Authentication failed: {str(e)}")
            self.log_api_result("get_auth_token", None, False)
            return False

    def get_network_devices(self):
        if not self.token:
            return None
        try:
            url = f"https://{DNAC['host']}:{DNAC['port']}/api/v1/network-device"
            headers = {"X-Auth-Token": self.token}
            response = requests.get(url, headers=headers, verify=False, timeout=10)
            response.raise_for_status()
            self.log_api_result("get_network_devices", None, True)
            return response.json().get('response', [])
        except Exception as e:
            print(f"❌ Failed to get devices: {str(e)}")
            self.log_api_result("get_network_devices", None, False)
            return None

    def get_device_interfaces(self, device_ip):
        if not self.token:
            return None
        try:
            devices = self.get_network_devices()
            device = next((d for d in devices if d.get('managementIpAddress') == device_ip), None)
            if not device:
                self.log_api_result("get_device_interfaces", device_ip, False)
                return None
            url = f"https://{DNAC['host']}:{DNAC['port']}/api/v1/interface"
            headers = {"X-Auth-Token": self.token}
            params = {"deviceId": device['id']}
            response = requests.get(url, headers=headers, params=params, verify=False, timeout=10)
            response.raise_for_status()
            self.log_api_result("get_device_interfaces", device_ip, True)
            return response.json().get('response', [])
        except Exception as e:
            print(f"❌ Failed to get interfaces: {str(e)}")
            self.log_api_result("get_device_interfaces", device_ip, False)
            return None
