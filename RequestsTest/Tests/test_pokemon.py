import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '276d1603e929f2a274276e236187b901'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '33826'
def test_status_code():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID} )
    assert responce.status_code == 200

def test_trainer_name():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID} )  
    assert responce.json()['data'][0]['trainer_name'] == 'ПокеБоул'
