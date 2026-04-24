from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route('/')
def index():
    current_year = datetime.datetime.now().year
    return render_template('index.html', number=random.randint(1, 100), year=current_year)


@app.route('/guess/<name>')
def guess(name):
    gender = requests.get('https://api.genderize.io/?name=' + name).json()['gender']
    age = requests.get('https://api.agify.io/?name=' + name).json()['age']
    return render_template('guess.html', name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
