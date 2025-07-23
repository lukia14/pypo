from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
csrf = CSRFProtect(app)
bd = SQLAlchemy(app)
app.config.from_pyfile('config.py')

from views import *

if __name__ == '__main__':
    app.run(debug=True)