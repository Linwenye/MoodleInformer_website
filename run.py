from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from flask import request
from utils import verify,encrypt
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config.from_object('config')

Bootstrap(app)
mongo = PyMongo(app)


def insert_db(email, password):
    mongo.db.users.insert_one({'email': email, 'password': password})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    if not verify(email, password):
        return render_template('fail.html')
    else:
        password = encrypt(password)
        if mongo.db.users.find_one({'email': email}):
            mongo.db.users.update_one({'email': email}, {'$set': {'password': password}})
        else:
            insert_db(email, password)
    return render_template('inform.html')


@app.route('/test')
def test():
    return render_template('inform.html')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',threaded=True)
