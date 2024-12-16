from sqlalchemy import CheckConstraint
from utils.mysql import db

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(100), nullable=False)
    Descripcion = db.Column(db.TEXT, nullable=False)
    estado = db.Column(db.String(20), default="Pendiente")

    __table_args__ = (
        CheckConstraint('estado IN ("Pendiente", "Completada")', name='check_estado'),
    )

    def __init__(self, Titulo, Descripcion,estado):
        self.Titulo = Titulo
        self.Descripcion = Descripcion
        self.estado = estado

    def __repr__(self):
        return f'<Tarea {self.Titulo}>'    