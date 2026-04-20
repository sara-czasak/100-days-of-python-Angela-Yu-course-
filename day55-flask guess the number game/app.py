from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/secret')
def secret():
    return '<h1>What do you call a well-balanced horse?\n<em>STABLE<em></h1>'


if __name__ == '__main__':
    app.run(debug=True)