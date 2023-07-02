import os
from dotenv import load_dotenv

load_dotenv()

MERAKI_DASHBOARD_API_KEY=os.getenv("MERAKI_DASHBOARD_API_KEY")
ORG_ID=os.getenv("ORG_ID")
NETWORK_ID=os.getenv("NETWORK_ID")
