from datetime import date
import json
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/meals/day')
def meals_today():
    url = "http://openmensa.org/api/v2/canteens/33/days/{0}/meals".format(date.today().isoformat())
    page = requests.get(url)
    meal_filter = lambda meal: {"name": meal["name"], "price": meal["prices"]["students"]}
    return json.dumps(map(meal_filter, page.json()), indent=4, separators=(',', ': '))


if __name__ == '__main__':
    app.run(debug=True)
