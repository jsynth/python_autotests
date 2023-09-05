import requests
import pytest

host = "https://dummyapi.io/data/v1"
headers= {"app-id": "64f71ad23fb07a9205d09849"}
id = "64f7232fa9de561d5f59c1f7"

def test_status_code():
    response = requests.get(f'{host}/post', headers=headers)
    assert response.status_code == 200

def test_part_of_answer():
     response = requests.get(f'{host}/user/{id}', headers=headers)
     assert response.json()['firstName'] == 'nika'

@pytest.mark.parametrize('key, value', [('firstName', 'nika'),
                                        ('lastName', 'petrova'),
                                        ('email', 'test6969@email.com')])
def test_part_of_answer(key, value):
    response = requests.get(f'{host}/user/{id}', headers=headers)
    assert response.json()[key] == value