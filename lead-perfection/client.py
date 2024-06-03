from . import utils


class Client(object):
    def __init__(self, serverid, clientid, username, password, appkey):
        self.serverid = serverid
        self.clientid = clientid
        self.username = username
        self.password = password
        self.appkey = appkey

    def get_credentials(self):
        return {
            'serverid': self.serverid,
            'clientid': self.clientid,
            'username': self.username,
            'password': self.password,
            'appkey':   self.appkey
        }

    def update_credentials(self, **kwargs):
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

    def authenticate(self):
        data = {
            'grant_type': 'password',
            'username': self.username,
            'password': self.password,
            'clientid': self.clientid,
            'appkey': self.appkey
        }

        url = f'https://{self.serverid}.leadperfection.com/token'

        headers = {
            'accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        try:
            response_data = utils.make_request(url=url, data=data, headers=headers)
            return response_data
        except (utils.ConnectionError, utils.Timeout, utils.HTTPError, utils.RequestException,
                utils.json.JSONDecodeError) as e:
            return f'Error: {e}'

