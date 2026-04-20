from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/secret')
def secret():
    return '<h1 style="text-align:center">What do you call a well-balanced horse?</h1><br><h2 style="text-align:center">STABLE</h2><h3 style="text-align:center">😂😂😂</h3>'


if __name__ == '__main__':
    app.run(debug=True)