from app import db

class Rol(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column('name', db.String(50), unique=True, nullable=False)  # Mapeando 'name' a 'nombre'
    descripcion = db.Column(db.Text)

    usuarios = db.relationship('Usuario', lazy=True)

