from flask import Flask
from routes.task import tasks
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from utils.mysql import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

app.secret_key = os.getenv('FLASK')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:" + os.getenv('PASSWORD') + "@localhost/tareasdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(tasks)

# Instancias base de datos
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
