from flask import Flask
# from sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import render_template
from flask import request
from verify import verify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config.from_object('config')

Bootstrap(app)
mongo = PyMongo(app)


def insert_db(email, password):
    pass


def existed(email):
    pass


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    if existed(email):
        pass
    if verify(email, password):
        pass
    print(email)
    print(password)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0',threaded=True)
