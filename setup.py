import os
import subprocess
import requests
import shutil
import json
from threading import Thread

#get total number of pokemon
def get_poke_count():
    url = 'https://pokeapi.co/api/v2/pokemon-species/'
    response = requests.get(url, stream=True)
    if response.status_code==200:
        json_data = json.loads(response.text)
        print('\n** Pokemon count found. Initializing download of data. **\n')
        return json_data['count']
    else:
        print(str(response.status_code) + ' error')

#download images for every pokemon
def get_images():
    for num in range(1 , poke_total+1):
        poke_number = format(num, '03d')
        url = 'https://www.serebii.net/pokemon/art/' + poke_number + '.png'
        path = 'pokedex/static/pokemon/pics/' + poke_number + '.png'
        exists = os.path.isfile(path)
        if exists:
            print('Image for #' + poke_number + ' already exists.')
        else:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(path, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response
                print('Pokemon image for #' + poke_number + ' downloaded.')
                if num == poke_total:
                    print('\n** Pokemon image directory download complete. **\n')
                num+=1
            else:
                print(str(response.status_code) + ' error')
                break
            

#setup info for every pokemon
def get_data():
    for num in range(1 , poke_total+1):
        poke_number = str(num)
        url_1 = 'https://pokeapi.co/api/v2/pokemon/' + poke_number + '/'
        url_2 = 'https://pokeapi.co/api/v2/pokemon-species/' + poke_number + '/'
        path = 'pokedex/static/pokemon/json/'
        response_1 = requests.get(url_1, stream=True)
        response_2 = requests.get(url_2, stream=True)
        if response_1.status_code==200 and response_2.status_code==200:
            json_data_1 = json.loads(response_1.text)
            json_data_2 = json.loads(response_2.text)
            for item in range(len(json_data_2['flavor_text_entries'])):
                if json_data_2['flavor_text_entries'][item]['language']['name'] == 'en':
                    description = json_data_2['flavor_text_entries'][item]['flavor_text']
                    break
            poke_data = {
                'name' : json_data_1['name'].title(),
                'number' : json_data_1['id'],
                'number_label' :  format(json_data_1['id'], '03d'),
                'height' : json_data_1['height'],
                'weight' : json_data_1['weight'],
                'color' : json_data_2['color']['name'].title(),
                'description' : description,
                'gen' : json_data_2['generation']['name']
            }
            pokemon = json.dumps(poke_data)
            
            f = open(path + format(json_data_1['id'], '03d') + '_' + json_data_1['name'] + '.json', 'w')
            f.write(pokemon)
            print('Pokemon data for for ' + str(num) + '-' + json_data_1['name'] + ' downloaded.')
            if num == poke_total:
                print('\n** Pokemon data directory download complete. **\n')
        else:
            print(str(response_1.status_code) + ' for response 1 and ' + str(response_2.status_code) + ' for response 2.')
            break

#terminal commands to run the app
def run_commands():
    subprocess.call(["pipenv", "install"])
    os.chdir('pokedex')
    subprocess.call(["py", "app.py"])

if __name__ == '__main__':
    #poke_total = get_poke_count()
    poke_total = 150
    if poke_total!=None and type(poke_total)==int:
        t1 = Thread(target = get_images)
        t2 = Thread(target = get_data)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        run_commands()
    else:
        print('Error, poke_total not a number or not set.')