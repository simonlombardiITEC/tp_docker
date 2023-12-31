import os

from flask import Flask
from flask_jwt_extended import (
    JWTManager,
)
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)   

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://DB2021:DB2021itec@143.198.156.171/Lombardi2'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') 
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
ma = Marshmallow(app)

load_dotenv()

from app.views import view
