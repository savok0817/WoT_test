import requests

url = 'https://api.worldoftanks.ru/wot/account/'
application_id = 'ecd581ab8edce9d383d6e67e0e22a5f0'


def search_account_id():
    payload = {'application_id': application_id, 'search': 'test_wgrs'}
    response = requests.post(url + 'list/', params=payload)
    loaded_data = response.json()
    account_id = str(loaded_data["data"][0]["account_id"])
    return account_id


def test_number_of_tank_battles():
    account_id = search_account_id()
    tank_id = '129'
    payload = {'application_id': application_id, 'account_id': account_id, 'tank_id': tank_id}
    response = requests.post(url + 'tanks/', params=payload)
    print('getting response by url = ' + response.url)
    loaded_data = response.json()
    battles_count = loaded_data["data"]["99001314"][0]["statistics"]["battles"]
    assert battles_count == 3, "Number of battles for the tank_id=129 doesn't equal to 3"


def test_general_number_of_tanks_for_user():
    account_id = search_account_id()
    payload = {'application_id': application_id, 'account_id': account_id}
    response = requests.post(url + 'tanks/', params=payload)
    print('getting response by url = ' + response.url)
    loaded_data = response.json()
    tanks_count = len(list(loaded_data["data"]["99001314"]))
    assert tanks_count == 5, "General number of tanks for user doesn't equal to 5"


def test_check_tank_id_presence_for_user():
    account_id = search_account_id()
    tank_id = '3089'
    payload = {'application_id': application_id, 'account_id': account_id, 'tank_id': tank_id}
    response = requests.post(url + 'tanks/', params=payload)
    print('getting response by url = ' + response.url)
    loaded_data = response.json()
    tanks_count = len(list(loaded_data["data"]["99001314"]))
    assert tanks_count == 1, "Number of found tanks for the user is not equal to 1"
    actual_tank_id = str(loaded_data["data"]["99001314"][0]["tank_id"])
    assert actual_tank_id == tank_id, "Tank with not expected id was found"
