"""Set up a flask app that retrieves the top technology news stories today."""

import flask
from NYTsecrets import api_key
import json
import requests


app = flask.Flask(__name__)

@app.route('/')
def welcome():
    """Utilize the template to show a welcome page."""
    return flask.render_template('index.html')

@app.route('/name/<name>')
def welcome_name(name):
    """Utilize the template to incorporate an individual's name."""
    return flask.render_template('name.html', name=name)


@app.route('/headlines/<name>')
def headlines(name):
    """Retrieve the top 5 articles from the New York Times."""
    url = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key="
    url_to_search = url + api_key
    response = requests.get(url_to_search)  
    news_list = json.loads(response.text)['results']
    return flask.render_template('headlines.html', news_list=news_list, name=name)


if __name__ == '__main__':
    app.run(debug=True)