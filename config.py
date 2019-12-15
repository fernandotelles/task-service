import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'tasks.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SECRET_KEY'] = '6a3056ebd17c729caeca5742'
db = SQLAlchemy(app)
CORS(app)