from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import os

app = Flask(__name__)

# ---------------------
# Konfiguracja bazy
# ---------------------
DB_HOST = "dpg-d2e5n4ggjchc73e2e6i0-a"
DB_PORT = "5432"
DB_NAME = "magazyn_wwo2"
DB_USER = "abc"
DB_PASS = "xruiiXquETHElmravuoxAXv5wUMuzs2l"

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------------
# Modele bazy danych
# ---------------------
class Magazyn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa_produktu = db.Column(db.String(100), nullable=False)
    ilosc = db.Column(db.Integer, nullable=False)

class BOM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produkt_id = db.Column(db.Integer, db.ForeignKey('magazyn.id'))
    komponent = db.Column(db.String(100), nullable=False)
    ilosc = db.Column(db.Integer, nullable=False)

class Produkcja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produkt_id = db.Column(db.Integer, db.ForeignKey('magazyn.id'))
    ilosc = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default="W trakcie")

# ---------------------
# Widoki frontend
# ---------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/magazyn/view')
def view_magazyn():
    produkty = Magazyn.query.all()
    return render_template('magazyn.html', produkty=produkty)

@app.route('/bom/view')
def view_bom():
    bom = BOM.query.all()
    return render_template('bom.html', bom=bom)

@app.route('/produkcja/view')
def view_produkcja():
    produkcja = Produkcja.query.all()
    return render_template('produkcja.html', produkcja=produkcja)

# ---------------------
# API endpoints (JSON)
# ---------------------
@app.route('/api/magazyn', methods=['GET'])
def api_magazyn():
    produkty = Magazyn.query.all()
    return jsonify([{'id': p.id, 'nazwa_produktu': p.nazwa_produktu, 'ilosc': p.ilosc} for p in produkty])

@app.route('/api/magazyn', methods=['POST'])
def api_add_magazyn():
    data = request.get_json()
    p = Magazyn(nazwa_produktu=data['nazwa_produktu'], ilosc=data['ilosc'])
    db.session.add(p)
    db.session.commit()
    return jsonify({'status': 'ok', 'id': p.id})

@app.route('/api/bom', methods=['GET'])
def api_bom():
    bom = BOM.query.all()
    return jsonify([{'id': b.id, 'produkt_id': b.produkt_id, 'komponent': b.komponent, 'ilosc': b.ilosc} for b in bom])

@app.route('/api/produkcja', methods=['GET'])
def api_produkcja():
    prod = Produkcja.query.all()
    return jsonify([{'id': p.id, 'produkt_id': p.produkt_id, 'ilosc': p.ilosc, 'status': p.status} for p in prod])

# ---------------------
# Uruchomienie
# ---------------------
if __name__ == '__main__':
    # Tworzenie tabel, jeśli nie istnieją
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
