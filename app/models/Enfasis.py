from app import db

class Enfasis(db.Model):
    __tablename__ = 'enfasis'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    
    usuarios = db.relationship('Usuario', lazy=True, cascade="all, delete")
