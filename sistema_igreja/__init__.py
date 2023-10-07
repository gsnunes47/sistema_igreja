from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask('__main__', template_folder=r'sistema_igreja\templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

from sistema_igreja import routes
