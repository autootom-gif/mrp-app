from flask import Flask, render_template, request, redirect
from config import Config
from models import db, Produkt, Komponent, BOM, Przyjecie, Produkcja

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# Magazyn
@app.route('/magazyn')
def magazyn():
    produkty = Produkt.query.all()
    return render_template('magazyn.html', produkty=produkty)

@app.route('/dodaj_produkt', methods=['POST'])
def dodaj_produkt():
    nazwa = request.form['nazwa']
    ilosc = int(request.form['ilosc'])
    produkt = Produkt(nazwa=nazwa, stan=ilosc)
    db.session.add(produkt)
    db.session.commit()
    return redirect('/magazyn')

# Komponenty
@app.route('/bom')
def bom():
    boms = BOM.query.all()
    produkty = Produkt.query.all()
    komponenty = Komponent.query.all()
    return render_template('bom.html', boms=boms, produkty=produkty, komponenty=komponenty)

@app.route('/dodaj_bom', methods=['POST'])
def dodaj_bom():
    produkt_id = int(request.form['produkt_id'])
    komponent_id = int(request.form['komponent_id'])
    ilosc = int(request.form['ilosc'])
    db.session.add(BOM(produkt_id=produkt_id, komponent_id=komponent_id, ilosc=ilosc))
    db.session.commit()
    return redirect('/bom')

# Produkcja
@app.route('/produkcja')
def produkcja():
    produkcje = Produkcja.query.all()
    produkty = Produkt.query.all()
    return render_template('produkcja.html', produkcje=produkcje, produkty=produkty)

@app.route('/dodaj_produkcje', methods=['POST'])
def dodaj_produkcje():
    produkt_id = int(request.form['produkt_id'])
    ilosc = int(request.form['ilosc'])
    db.session.add(Produkcja(produkt_id=produkt_id, ilosc=ilosc))
    db.session.commit()
    return redirect('/produkcja')

# Przyjęcia magazynowe
@app.route('/przyjecia')
def przyjecia():
    przyjecia = Przyjecie.query.all()
    komponenty = Komponent.query.all()
    return render_template('przyjecia.html', przyjecia=przyjecia, komponenty=komponenty)

@app.route('/dodaj_przyjecie', methods=['POST'])
def dodaj_przyjecie():
    komponent_id = int(request.form['komponent_id'])
    ilosc = int(request.form['ilosc'])
    db.session.add(Przyjecie(komponent_id=komponent_id, ilosc=ilosc))
    komponent = Komponent.query.get(komponent_id)
    db.session.commit()
    return redirect('/przyjecia')

if __name__ == '__main__':
    app.run(debug=True)
