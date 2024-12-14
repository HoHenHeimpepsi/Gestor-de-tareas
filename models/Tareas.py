from utils.mysql import db

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.TEXT, nullable=False)

    def __init__(self, Titulo, Descripcion):
        self.Titulo = Titulo
        self.Descripcion = Descripcion