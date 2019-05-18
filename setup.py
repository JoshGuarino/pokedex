import requests
import shutil
import json
from threading import Thread


#download images for every pokemon
def get_images():
    num = 800
    while True:
        poke_number = format(num, '03d')
        url = 'https://www.serebii.net/pokemon/art/' + poke_number + '.png'
        path = 'pokedex/static/pokemon/pics/' + poke_number + '.png'
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            print('Pokemon image for #' + poke_number + ' downloaded.')
            num+=1
        elif response.status_code == 404:
            print('\n** Pokemon image directory download complete. **\n')
            break
        else:
            print(response.status_code + ' error')

#setup info for every pokemon
def get_data():
    num = 800
    while True:
        poke_number = str(num)
        url_1 = 'https://pokeapi.co/api/v2/pokemon/' + poke_number + '/'
        url_2 = 'https://pokeapi.co/api/v2/pokemon-species/' + poke_number + '/'
        path = 'pokedex/static/pokemon/json/'
        response_1 = requests.get(url_1, stream=True)
        response_2 = requests.get(url_2, stream=True)
        if response_1.status_code==200 and response_2.status_code==200:
            json_data_1 = json.loads(response_1.text)
            json_data_2 = json.loads(response_2.text)
            poke_data = {
                'name' : json_data_1['name'],
                'number' : json_data_1['id'],
                'height' : json_data_1['height'],
                'weight' : json_data_1['weight'],
                'color' : json_data_2['color']['name'],
                'description' : json_data_2['flavor_text_entries'][2]['flavor_text']
            }
            pokemon = json.dumps(poke_data)
            f = open(path + str(json_data_1['id']) + '_' + json_data_1['name'] + '.json', 'w')
            f.write(pokemon)
            print('Pokemon data for for ' + json_data_1['name'] + ' downloaded.')
            num+=1
        elif response_1.status_code==404 and response_2.status_code==404:
            print('\n** Pokemon data directory download complete. **\n')
            break
        else:
            print(response_1.status_code + 'for response 1 and ' + response_2.status_code + ' for response 2.')
    
    

if __name__ == '__main__':
    Thread(target = get_images).start()
    Thread(target = get_data).start()
