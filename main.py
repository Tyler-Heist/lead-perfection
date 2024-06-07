import importlib
import json

# FIXME: Incorporate later?
"""if not isinstance(self.access_token, str):
    return f"access_token: Expected type 'str', got '{str(type(self.access_token))[8:-2]}' instead"""

LP = importlib.import_module('lead-perfection.client')
sales = importlib.import_module('lead-perfection.sales')

client = LP.Client('apitest', 'demo3', 'demo3api', 'LP3api123!', '4E405C4F-6EAA-4A7F-A0AE-5B955B1FD2F1')
auth_data = client.authenticate()
access_token = auth_data['access_token']
print(access_token)

# access_token = ''
# if isinstance(auth_data, dict) and 'access_token' in auth_data:
#     access_token = auth_data['access_token']
# with open('auth_data.json', 'w') as outfile:
#     outfile.write(json.dumps(auth_data, indent=4))

sale = sales.Sales(server_id='apitest', access_token=access_token)
result = sale.get_links('cst', 2727)
print(result)







