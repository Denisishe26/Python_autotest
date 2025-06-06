import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '276d1603e929f2a274276e236187b901'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "pirojok",
    "photo_id": 8
}
body_change = {
    "pokemon_id": "332492",
    "name": "kolobok",
    "photo_id": 9
}
body_add = {
    "pokemon_id": "332492"
}

# Создать покемона
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''


# Сменить имя покемона
'''response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_create.text)'''

# Поймать в покебол
response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_create.text)




