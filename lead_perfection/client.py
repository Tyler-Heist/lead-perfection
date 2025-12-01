from dataclasses import dataclass

import requests.exceptions

from . import utils


@dataclass
class Client:
    """
    A client wrapper for authenticating and interacting with the LeadPerfection API.

    Parameters:
        server_id (str): The LeadPerfection server to connect to.
            - Use `'apitest'` when working with LP's test/sandbox servers.
            - Use `'api'` for production environments (real customer data).
        client_id (str): The client/application ID.
        username (str): Username for API authentication.
        password (str): Password for API authentication.
        app_key (str): Application key provided by LeadPerfection.
    """

    server_id: str
    client_id: str
    username: str
    password: str
    app_key: str

    def __post_init__(self):
        # Validate fields early
        fields = {
            "server_id": self.server_id,
            "client_id": self.client_id,
            "username": self.username,
            "password": self.password,
            "app_key": self.app_key
        }
        for name, value in fields.items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string.")

    def get_credentials(self) -> dict:
        return {
            'serverid': self.server_id,
            'clientid': self.client_id,
            'username': self.username,
            'password': self.password,
            'appkey':   self.app_key
        }

    def update_credentials(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

    def authenticate(self) -> dict:
        data = {
            'grant_type': 'password',
            'username': self.username,
            'password': self.password,
            'clientid': self.client_id,
            'appkey': self.app_key
        }

        url = f'https://{self.server_id}.leadperfection.com/token'

        headers = {
            'accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        if not all([self.server_id, self.client_id, self.username, self.password, self.app_key]):
            raise ValueError("All Client parameters must be non-empty strings.")

        try:
            return utils.make_post_request(url=url, data=data, request_headers=headers)
        except requests.exceptions.RequestException as e:
            raise AuthenticationError(f'Authentication failed: {e}') from e
        except RuntimeError as e:
            raise AuthenticationError(f'Authentication Failed (invalid JSON response): {e}') from e


class AuthenticationError(Exception):
    pass