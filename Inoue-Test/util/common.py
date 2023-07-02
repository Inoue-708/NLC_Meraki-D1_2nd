import requests
from util.settings import *

def GetClientsList():
    url = f"https://api.meraki.com/api/v1/organizations/{ORG_ID}/networks/{NETWORK_ID}/clients"
    headers = {
        'X-Cisco-Meraki-API-Key': MERAKI_DASHBOARD_API_KEY,
        'Content-Type': 'application/json'
    }
    return requests.get(url, headers=headers)


def GetSensoratewayInfo(sensor_serial):
    url = f"https://api.meraki.com/api/v1/devices/{sensor_serial}/sensor/relationships"
    headers = {
        'X-Cisco-Meraki-API-Key': MERAKI_DASHBOARD_API_KEY,
        'Content-Type': 'application/json'
    }
    return requests.get(url, headers=headers)
