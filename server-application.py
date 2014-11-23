from datetime import date
from flask import Flask, Response, json
import requests
from flask.ext.cache import Cache


app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'redis'})


@app.route('/')
def meals_today():
    return meals_day(date.today().isoformat())

@app.route('/meals/day/<day>/')
@cache.cached(timeout=3600)
def meals_day(day):
    url = "http://openmensa.org/api/v2/canteens/33/days/{0}/meals".format(day)
    page = requests.get(url)
    meal_format = lambda meal: {"name": meal["name"],
                                "price": meal["prices"]["students"]}
    result = map(meal_format , page.json())
    json_result = json.dumps(result, indent=1, ensure_ascii=False).encode('utf8')
    return Response(json_result, content_type='application/json;charset=utf-8')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
