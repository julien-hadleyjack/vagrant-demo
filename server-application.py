from datetime import date
import json
from flask import Flask
import requests
from flask.ext.cache import Cache


app = Flask(__name__)
app.config.from_object('config')

cache = Cache(app, config={'CACHE_TYPE': 'redis'})


@app.route('/')
@app.route('/meals/day/')
def meals_today():
    return meals_day(date.today().isoformat())


@app.route('/meals/day/<day>/')
@cache.cached(timeout=3600)
def meals_day(day):
    url = "http://openmensa.org/api/v2/canteens/33/days/{0}/meals".format(day)
    page = requests.get(url)
    meal_filter = lambda meal: {"name": meal["name"], "price": meal["prices"]["students"]}
    return json.dumps(map(meal_filter, page.json()), indent=2, separators=(',', ': '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=app.config['PORT'])
