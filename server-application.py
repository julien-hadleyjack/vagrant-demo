from datetime import date
import json
from flask import Flask
import requests
import re


app = Flask(__name__)

@app.route('/')
@app.route('/meals/day/')
@app.route('/meals/day/<day>/')
def meals_day(**day):
    day = date.today().isoformat() if not day else day["day"]
    url = "http://openmensa.org/api/v2/canteens/33/days/{0}/meals".format(day)
    page = requests.get(url)
    meal_filter = lambda meal: {"name": meal["name"], "price": meal["prices"]["students"]}
    return json.dumps(map(meal_filter, page.json()), indent=2, separators=(',', ': '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
