import pytest
from Model.players import *
from Model.utils import *
from Model.properties import *


def test_login_with_wrong_user():

    data = Properties.get()
    query = {'page': "1"}
    response = requests.get(data.envProperties['url'],
                            params=query,
                            auth=HTTPBasicAuth(get_random_string(6), data.envProperties['password']))

    assert response.status_code != 200, "Login with wrong user succeed!"


def test_login_with_wrong_password():

    data = Properties.get()
    query = {'page': "1"}
    response = requests.get(data.envProperties['url'],
                            params=query,
                            auth=HTTPBasicAuth(data.envProperties['username'], get_random_string(6)))

    assert response.status_code != 200, "Login with wrong password succeed!"


def test_wrong_url_parameter_value():

    data = Properties.get()
    query = {'page': "AAA"}
    response = requests.get(data.envProperties['url'],
                            params=query,
                            auth=HTTPBasicAuth(data.envProperties['username'], data.envProperties['password']))

    assert response.status_code == 400, \
        "Response status of request with wrong url parameter value: expected 400, but actual: " + str(response.status_code)


def test_wrong_url_parameter_key():

    data = Properties.get()
    query = {'AAA': "1"}
    response = requests.get(data.envProperties['url'],
                            params=query,
                            auth=HTTPBasicAuth(data.envProperties['username'], data.envProperties['password']))

    assert response.status_code == 400, \
        "Response status of request with wrong url parameter key: expected 400, but actual: " + str(response.status_code)


def test_get_players():
    players = get_players()
    assert len(players) > 0


def test_get_page_with_non_existing_index():
    players = get_players(10000000) # Assuming I know the number of players in DB
    assert len(players) == 0, "Expected empty list. Received list of players:" + str(players)


pages=[1,2,17]


# Check that both Name and ID contain values
@pytest.mark.parametrize('arg', pages)
def test_values_not_empty(arg):
    players = get_players(arg)
    errors = []

    for player in players:
        if player['Name'] == "" or player['Name'] == "null":
            errors.append("Found player with empty name. Player ID:" + str(player['ID']))
        if player['ID'] is None:
            errors.append("Found player with empty ID. Player Name:" + str(player['Name']))

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))


def test_ids_are_sequential():
    players = get_players(1)
    errors = []
    current_id = -1
    for player in players:
        if current_id == -1:
            current_id = player['ID']
            break

        current_id = current_id + 1
        if player['ID'] != current_id:
            errors.append("Found non-sequential ID: " + player['ID'] + " for Player:" + str(player['Name']))

    assert not errors, "errors occurred:\n{}".format("\n".join(errors))




