#!/usr/local/bin/python3
import requests
import json

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
        
    # Get user stats
    def get_user_stats(self, user_num, season_id):
        url = f'{self.api_url}/user/stats/{user_num}/{season_id}'
        r = requests.get(url, headers=self.http_header)
        r_json = json.dumps(r.json())
        r_data = json.loads(r_json)
        
        if r.status_code == 200:
            return r_data
            
    # Get user games
    def get_user_games(self, user_num):
        url = f'{self.api_url}/user/games/{user_num}'
        r = requests.get(url, headers=self.http_header)
        r_json = json.dumps(r.json())
        r_data = json.loads(r_json)
        
        if r.status_code == 200:
            return r_data
            
    # Get game details
    def get_game_details(self, game_id):
        url = f'{self.api_url}/games/{game_id}'
        r = requests.get(url, headers=self.http_header)
        r_json = json.dumps(r.json())
        r_data = json.loads(r_json)
        
        if r.status_code == 200:
            return r_data