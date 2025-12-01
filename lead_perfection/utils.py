import json
import requests


def headers(access_token: str = None):
    return {
        'Authorization': f'Bearer {access_token}',
        'accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded'
    }


def make_post_request(url: str, data: dict, request_headers: dict) -> dict:
    try:
        response = requests.post(url=url, data=data, headers=request_headers)
        response.raise_for_status()
        try:
            return response.json()
        except json.decoder.JSONDecodeError as je:
            raise RuntimeError(f"Failed to decode JSON response: {je}") from je
    except requests.exceptions.RequestException:
        raise


def make_get_request(url: str, params: dict, request_headers: dict) -> dict:
    try:
        response = requests.get(url=url, params=params, headers=request_headers)
        response.raise_for_status()
        try:
            return response.json()
        except json.decoder.JSONDecodeError as je:
            raise RuntimeError(f"Failed to decode JSON response: {je}") from je
    except requests.exceptions.RequestException:
        raise

