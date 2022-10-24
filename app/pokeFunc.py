import requests as req

def getPokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    resp = req.get(url)                 # requested URL for pokemon by name or number
    if resp.ok:
        dct = resp.json()
        pokemon_dict = {'name': dct['name'],    # forms dictionary to be returned as requested by instructor
            'ability': dct['abilities'][0]['ability']['name'],
            'base_experience': dct['base_experience'],
            'official_artwork': dct['sprites']['other']['official-artwork']['front_default'],
            'hp': dct['stats'][0]['base_stat'],
            'attack': dct['stats'][1]['base_stat'],
            'defense': dct['stats'][2]['base_stat'],
            'special_attack': dct['stats'][3]['base_stat'],
            'special_defense': dct['stats'][4]['base_stat'],
            'speed': dct['stats'][5]['base_stat']
            }
        return pokemon_dict
    else:
        return 'I don\'t know that Pokemon. Did you spell the name correctly?'