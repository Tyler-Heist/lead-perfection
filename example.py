import lead_perfection as lp

client = lp.client.Client('apitest', 'demo3', 'demo3api', 'LP3api123!', '4E405C4F-6EAA-4A7F-A0AE-5B955B1FD2F1')
auth_data = client.authenticate()
access_token = auth_data['access_token']
print(access_token)

lp_menu = lp.menu.Menu(server_id='apitest', access_token=access_token)
result = lp_menu.get_menu()
print(result)







