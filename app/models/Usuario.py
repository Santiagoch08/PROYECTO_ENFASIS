from app import db

class Usuario(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    enfasis_id = db.Column(
      db.Integer,
      db.ForeignKey('enfasis.id'),
      nullable=False
    )
    
    role = db.Column(
      db.Integer,
      db.ForeignKey('roles.id'),
      nullable=False
    )

    enfasis = db.relationship('Enfasis', lazy=True)
    rol = db.relationship('Rol', backref=db.backref('usuarios', lazy=True))