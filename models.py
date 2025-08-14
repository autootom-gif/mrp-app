from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produkt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), unique=True, nullable=False)
    stan = db.Column(db.Integer, default=0)

class Komponent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), unique=True, nullable=False)

class BOM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produkt_id = db.Column(db.Integer, db.ForeignKey('produkt.id'), nullable=False)
    komponent_id = db.Column(db.Integer, db.ForeignKey('komponent.id'), nullable=False)
    ilosc = db.Column(db.Integer, nullable=False)
    produkt = db.relationship('Produkt', backref=db.backref('bom', lazy=True))
    komponent = db.relationship('Komponent', backref=db.backref('bom', lazy=True))

class Przyjecie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    komponent_id = db.Column(db.Integer, db.ForeignKey('komponent.id'), nullable=False)
    ilosc = db.Column(db.Integer, nullable=False)
    komponent = db.relationship('Komponent', backref=db.backref('przyjecia', lazy=True))

class Produkcja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produkt_id = db.Column(db.Integer, db.ForeignKey('produkt.id'), nullable=False)
    ilosc = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='planowane')
    produkt = db.relationship('Produkt', backref=db.backref('produkcja', lazy=True))
