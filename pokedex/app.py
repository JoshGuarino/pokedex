from flask import Flask, render_template, request

from config import Config
import os
import json
import math


app = Flask(__name__)
app.config.from_object(Config)

pokemon_data = []
pokemon_directory = os.listdir('static/pokemon/json')
num_results = Config.RESULTS_PER_PAGE
for item in pokemon_directory:
    with open('static/pokemon/json/' + item , 'r') as file:
        data = file.read()
    pokemon = json.loads(data)
    pokemon_data.append(pokemon)

page_total = math.ceil(len(pokemon_data) / num_results)
pages = []
page_range_index = { 'start': 0, 'end': num_results }
for page in range(0, page_total):
    page = { 'start': page_range_index['start'] , 'end': page_range_index['end'] }
    pages.append(page)
    page_range_index['start'] += num_results
    page_range_index['end'] += num_results
    if page_range_index['end'] > len(pokemon_data):
        page_range_index['end'] = len(pokemon_data)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', data=pokemon_data, start=0, end=num_results, page_num=1, page_total=page_total)


@app.route('/<page>')
@app.route('/index/<page>')
def index_pages(page):
    try:
        page = int(page)
        current_page = pages[page-1]
    except ValueError:
        return render_template('error.html', the_error="To request page, param must be a number."), 404
    except:
        return render_template('error.html', the_error="The requested page doesn't exist."), 404
        
    if page < 1:
        return render_template('error.html', the_error="The requested page doesn't exist."), 404
    else:
        return render_template('index.html', data=pokemon_data, start=current_page['start'], end=current_page['end'], page_num=page, page_total=page_total)


@app.route("/pokemon")
def pokemon():
    return render_template('pokemon.html')


@app.route("/search", methods=['POST'])    
def search():
    query = request.form['search']
    return render_template('search.html', query=query)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', the_error=e), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', the_error=e), 500    

if __name__ == '__main__':
    app.run()