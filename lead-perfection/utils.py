import json
import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException


def make_request(url, data, headers):
    try:
        response = requests.post(url=url, data=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except ConnectionError as ce:
        return f'Connection Error: {ce}'
    except Timeout as te:
        return f'Request Timeout: {te}'
    except HTTPError as he:
        return f'HTTP Error: {he}'
    except RequestException as re:
        return f'Request Exception: {re}'
    except json.JSONDecodeError as je:
        return f'JSON Decode Error: {je}'
