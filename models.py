from app import db


class Usuario(db.Model):
    """Modelo Usuario"""
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    city = db.Column(db.String(100))

    def __repr__(self):
        return f'<User: {self.nombre}>'
