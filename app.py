from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def get_pokemon(query):
    r = requests.get('http://pokeapi.co/api/v2/pokemon/{}'.format(query))
    data = json.loads(r.text)
    if query.isdigit():
        name = data["name"]
        return '<h1>The pokemon with id {0} is {1}</h1>'.format(query, name)
    else:
        my_id = str(data["id"])
        return '<h1>{0} has id {1}</h1>'.format(query.title(), my_id)

app.add_url_rule('/pokemon/<query>', 'get_pokemon', get_pokemon)


if __name__ == '__main__':
    app.run()
