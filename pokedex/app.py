from flask import Flask, render_template
from config import Config
import os
import json

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
@app.route("/index")
def index():
    pokemon_directory = os.listdir('static/pokemon/json')
    pokemon_data = []
    for item in pokemon_directory:
        with open('static/pokemon/json/' + item , 'r') as file:
            data = file.read()
        pokemon = json.loads(data)
        pokemon_data.append(pokemon)
    return render_template('index.html', pokemon_data = pokemon_data, len = len(pokemon_data))

@app.route("/pokemon")
def pokemon():
    return render_template('pokemon.html')

if __name__ == '__main__':
    app.run()