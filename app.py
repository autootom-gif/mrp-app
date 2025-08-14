from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# --- MODELE ---
class Magazyn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa_produktu = db.Column(db.String(100), nullable=False)
    ilosc = db.Column(db.Integer, default=0)

class BOM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produkt_finalny = db.Column(db.String(100), nullable=False)
    komponent = db.Column(db.String(100), nullable=False)
    ilosc = db.Column(db.Integer, default=0)

class Produkcja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produkt_finalny = db.Column(db.String(100), nullable=False)
    ilosc = db.Column(db.Integer, default=0)

# --- ROUTES ---
@app.route('/')
def index():
    return "MRP App działa!"

# Magazyn
@app.route('/magazyn', methods=['GET'])
def get_magazyn():
    produkty = Magazyn.query.all()
    return jsonify([{'id': p.id, 'nazwa_produktu': p.nazwa_produktu, 'ilosc': p.ilosc} for p in produkty])

@app.route('/magazyn', methods=['POST'])
def add_magazyn():
    data = request.get_json()
    produkt = Magazyn(nazwa_produktu=data['nazwa_produktu'], ilosc=data.get('ilosc', 0))
    db.session.add(produkt)
    db.session.commit()
    return jsonify({'message': 'Produkt dodany'}), 201

# BOM
@app.route('/bom', methods=['GET'])
def get_bom():
    bom = BOM.query.all()
    return jsonify([{'id': b.id, 'produkt_finalny': b.produkt_finalny, 'komponent': b.komponent, 'ilosc': b.ilosc} for b in bom])

@app.route('/bom', methods=['POST'])
def add_bom():
    data = request.get_json()
    b = BOM(produkt_finalny=data['produkt_finalny'], komponent=data['komponent'], ilosc=data.get('ilosc',1))
    db.session.add(b)
    db.session.commit()
    return jsonify({'message':'BOM dodany'}), 201

# Produkcja
@app.route('/produkcja', methods=['POST'])
def add_produkcja():
    data = request.get_json()
    p = Produkcja(produkt_finalny=data['produkt_finalny'], ilosc=data.get('ilosc',1))
    db.session.add(p)
    db.session.commit()
    return jsonify({'message':'Produkcja dodana'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
