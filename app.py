import datetime
from flask import Flask, render_template, request
from flask_cors import CORS
from models import *
import time

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def index():

    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')
        name = request.form.get('name')
        post = request.form.get('post')
        createpost(timestamp, name, post)

    elif request.method == 'DELETE':
        reset()

    posts = getposts()

    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
