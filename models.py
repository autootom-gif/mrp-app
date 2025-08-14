from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Magazyn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa_produktu = db.Column(db.String(100), nullable=False)
    ilosc = db.Column(db.Integer, default=0)

class BOM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produkt = db.Column(db.String(100), nullable=False)
    komponent = db.Column(db.String(100), nullable=False)
    ilosc = db.Column(db.Integer, default=0)

class Produkcja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produkt = db.Column(db.String(100), nullable=False)
    ilosc_produkcji = db.Column(db.Integer, default=0)
