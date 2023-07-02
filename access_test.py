import sys
import meraki
import requests
from util.settings import *

print("-"*50)
print("Start API access.")
print(f"[API Key] {MERAKI_DASHBOARD_API_KEY}")
print("-"*50)

if not MERAKI_DASHBOARD_API_KEY:
    print ("Error: API Key NOT set.")
    sys.exit()
    
try:
    m = meraki.DashboardAPI(output_log=False)

    my_orgs = m.organizations.getOrganizations()
    my_nwid = m.organizations.getOrganizationNetworks(my_orgs[0]['id'])
    
    print("-"*50)
    print("API access succeeded.")
    print(f"[organization ID] {my_orgs[0]['id']}")
    print(f"[Network ID] {my_nwid[0]['id']}")
    print("-"*50)

except Exception as e:
    print("error:" + e)
    