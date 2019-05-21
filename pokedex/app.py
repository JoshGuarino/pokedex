from flask import Flask, render_template, request
from flask_paginate import Pagination
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
    return render_template('index.html', pokemon_data=pokemon_data, len=len(pokemon_data))

@app.route("/pokemon")
def pokemon():
    return render_template('pokemon.html')

@app.route("/search", methods=['POST'])    
def search():
    query = request.form['search']
    return render_template('search.html', query=query)

if __name__ == '__main__':
    app.run()