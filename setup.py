import requests
import shutil
import json

num = 1

#download images for every pokemon
while True:
    poke_number = format(num, '03d')
    url = 'https://www.serebii.net/pokemon/art/' + poke_number + '.png'
    path = 'pokedex/static/images/' + poke_number + '.png'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        print('Pokemon image for #' + poke_number + ' downloaded.')
        num+=1
    elif response.status_code == 404:
        print('Pokemon image directory download complete.')
        break
    else:
        print(response.status_code + ' error')

#setup info for every pokemon
for i in range(1, num):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(i) + '/'
    path = 'pokedex/static/pokemon/'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        poke_data = {
            'name' : json_data['name'],
            'number' : json_data['id']
        }
        pokemon = json.dumps(poke_data)
        f = open(path + str(json_data['id']) + '_' + json_data['name'] + '.json', 'w')
        f.write(pokemon)
        print('Pokemon data for for ' + json_data['name'] + ' downloaded.')
    elif response.status_code == 404:
         print('Pokemon data directory download complete.')
         break
    else:
         print(response.status_code + ' error')
    
    