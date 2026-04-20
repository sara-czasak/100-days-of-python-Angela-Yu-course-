from flask import Flask, render_template
import random


app = Flask(__name__)
random_number = random.randint(0,9)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<number>')
def game(number):
    number = int(number)
    if number > random_number:
        return f'<h1 style="color: purple; text-align: center">{number} is too high, try again!</h1><br><div style="text-align:center"><img width="300px" src="../static/images/too_high.webp"></div>'
    elif number < random_number:
        return f'<h1 style="color: red; text-align: center">{number} is too low, try again!</h1><br><div style="text-align:center"><img width="300px" src="../static/images/too_low.webp"></div>'
    else:
        return f'<h1 style="color: green; text-align: center">you guessed it! {number} is the number I was thinking of!</h1><br><div style="text-align:center"><img width="300px" src="../static/images/correct.webp"></div>'


@app.route('/secret')
def secret():
    return '<h1 style="text-align:center">What do you call a well-balanced horse?</h1><br><h2 style="text-align:center">STABLE</h2><h3 style="text-align:center">😂😂😂</h3>'


if __name__ == '__main__':
    app.run(debug=True)