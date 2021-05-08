#!/usr/local/bin/python3
import requests
import json
import sys

class ErbsClient(object):
    def __init__(self, api_key, version = 'v1'):
        self.api_key = api_key
        self.version = version
        self.api_url = f'https://open-api.bser.io/{self.version}'

    @property
    def http_header(self):
        return {
            'Accept': 'application/json',
            'X-API-Key': self.api_key,
        }

    # Get user number from user nickname/game name    
    def get_user_num(self, user_nickname):
        url = f'{self.api_url}/user/nickname/'
        r = requests.get(url, headers=self.http_header, params={('query', user_nickname),})
        r_json = json.dumps(r.json())
        r_data = json.loads(r_json)
        user_num = r_data['user']['userNum']
        return user_num
