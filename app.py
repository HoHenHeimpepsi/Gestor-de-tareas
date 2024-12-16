from flask import Flask
from routes.task import tasks
from routes.json_export import export
from routes.json_import import imports
from flask_sqlalchemy import SQLAlchemy
from models.Tareas import Tarea
from flask_wtf.csrf import CSRFProtect
from utils.mysql import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://root:{os.getenv('PASSWORD')}@localhost/tareasdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('FLASK')

db.init_app(app)

app.config['DEBUG'] = True

app.register_blueprint(tasks)
app.register_blueprint(export)
app.register_blueprint(imports)

# Instancias base de datos
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
