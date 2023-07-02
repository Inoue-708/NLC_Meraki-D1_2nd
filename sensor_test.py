import sys
from util.common import *

r=GetSensoratewayInfo("")

# Check if the request was successful
if r.status_code == 200:
    gw_device = r.json()
    print(f"Gateway Device Serial: {gw_device['livestream']['relatedDevices'][0]['serial']}")
    print(f"Gateway Device ProductType: {gw_device['livestream']['relatedDevices'][0]['productType']}")
    gw_serial=gw_device['livestream']['relatedDevices'][0]['productType']
else:
    print(f"Error: {r.status_code} - {r.text}")
    sys.exit()



