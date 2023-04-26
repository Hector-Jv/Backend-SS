from app import db

class Estudiante(db.Model):
    cve_estudiante = db.Column(db.Integer, primary_key=True)
    nombre_estudiante = db.Column(db.String(100), nullable=False)
    

    historial = db.relationship('Historial', backref='calificaciones')