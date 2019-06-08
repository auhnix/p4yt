import datetime
from flask import Flask, render_template, request
from flask_cors import CORS
from models import *
import time

app = Flask(__name__)

CORS(app)

app.jinja_env.globals.update(getuserposts=getuserposts)
app.jinja_env.globals.update(clean=clean)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')
        name = request.form.get('name')
        post = request.form.get('post')
        createpost(timestamp, name, post)

    posts = getposts()
    return render_template('index.html', posts=posts)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/users/<user>', methods=['GET'])
def userpg(user):
  return render_template('userpg.html', title='user details', user=user)

@app.route('/refresh')
def refresh():
    reset()

if __name__ == '__main__':
    app.run(debug=True)
