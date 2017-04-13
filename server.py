from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import requests

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/search', methods=['POST'])
def search():
    r = requests.get('https://api.tronalddump.io/search/quote?query=' + request.form['phrase'])
    return jsonify([x["value"] for x in r.json()['_embedded']['quotes']])

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# Test with command `curl -X POST http://127.0.0.1:5000/login`
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "login from POST\n"
    else:
        return "login from GET\n"

if __name__ == "__main__":
    app.run()
