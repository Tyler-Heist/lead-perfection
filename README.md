# lead-perfection
lead-perfection is a Python library that provides a simple interface for interaction with [LeadPerfection](https://app.swaggerhub.com/apis/LeadPerfection/Examples/1.0) methods, packaging them into an easy-to-use format. It abstracts authentication, request formatting, and endpoint access to make LeadPerfection integrations easier for developers building automations, backend services, and CRM tooling.

## Benefits & Features
- Simple authentication workflow
- Organized client and module structure (client, customers, leads, etc.)
- Reduces need to write boilerplate requests for LeadPerfection API calls

## Installation
```bash
pip install lead-perfection
```

## Usage Example
Here is a real-world example based on the library's example.py.  
Replace the credential values with your own LeadPerfection environment details.

```python
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
result = lp_menu.get_menu()

print("Menu Result:", result)
```

## Project Structure
 - `canvass.py` — Wrapper for all canvass-related API calls
 - `client.py` — Handles authentication with the LeadPerfection API
 - `custom.py` - Wrapper for custom API calls
 - `customers.py` - Wrapper for all customer-related API calls
 - `downloads.py` - Wrapper for all download-related API calls
 - `file.py` - Wrapper for all file-related API calls
 - `installer.py` - Wrapper for all installer-related API calls
 - `leads.py` — Wrapper for all lead-related API calls
 - `menu.py` — Wrapper for all menu-related API calls
 - `sales.py` - Wrapper for all sales-related API calls
 - `utils.py` - Abstraction for http requests and header setup

## Extending the Library
`lead-perfection` is structured so you can easily add new endpoint wrappers:
 - Create a new module file (e.g., `appointments.py`)
 - Implement functions that call the appropriate LeadPerfection API paths

## Requirements
- Python 3.8+

## License
This project is licensed under the MIT License.

## Links
- Source Code: https://github.com/Tyler-Heist/lead-perfection
- Issues: https://github.com/Tyler-Heist/lead-perfection/issues
