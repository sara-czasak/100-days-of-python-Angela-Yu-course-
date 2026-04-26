from flask import Flask, render_template
import requests


app = Flask(__name__)
all_posts = requests.get('https://api.npoint.io/c2ce5e603a4f0ad12819').json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<post_id>')
def post(post_id):
    post = all_posts[int(post_id)-1]
    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)
