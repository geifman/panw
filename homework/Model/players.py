import requests
from requests.auth import HTTPBasicAuth
from Model.properties import *


def get_players(page="1"):

    data = Properties.get()

    query = {'page': page}

    response = requests.get(data.envProperties['url'],
                            params=query,
                            auth=HTTPBasicAuth(data.envProperties['username'], data.envProperties['password']))

    if response.status_code != 200:
        raise ValueError('get_players failed with status code: ' + str(response.status_code) + ' and error message: ' + response.reason)

    return (response.json())

#def get_player_by_name

#def delete_player

#def update_player