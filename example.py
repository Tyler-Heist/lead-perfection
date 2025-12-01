import lead_perfection as lp

# Initialize the client
# Update each argument with your actual LeadPerfection credentials
client = lp.client.Client(
    'apitest',                          # server_id
    'demo3',                            # client_id
    'demo3api',                         # username
    'LP3api123!',                       # password
    '4E405C4F-6EAA-4A7F-A0AE-5B955B1FD2F1'  # app_key
)

# Authenticate and retrieve an access token
auth_data = client.authenticate()
access_token = auth_data['access_token']
print("Access Token:", access_token)

# Access the Menu endpoint using the obtained token
lp_menu = lp.menu.Menu(server_id='apitest', access_token=access_token)
menu_result = lp_menu.get_menu()

print("Menu Result:", menu_result)

# Access the Leads endpoint using the obtained token
lp_leads = lp.leads.Leads(server_id='apitest', access_token=access_token)
leads_result = lp_leads.leads_login_message()

print("Leads Login Message Result:", leads_result)