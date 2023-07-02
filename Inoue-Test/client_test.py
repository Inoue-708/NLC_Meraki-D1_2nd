from util.common import *

r=GetClientsList()

# Check if the request was successful
if r.status_code == 200:
    clients = r.json()
    # Process the list of clients
    for client in clients:
        print(f"Client MAC: {client['mac']}, IP: {client['ip']}, Description: {client['description']}")
else:
    print(f"Error: {r.status_code} - {r.text}")
    