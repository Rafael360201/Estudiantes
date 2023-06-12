from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    correo_electronico = db.Column(db.String(100))

    def __init__(self, nombre_completo, edad, correo_electronico):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.correo_electronico = correo_electronico
