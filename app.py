from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Magazyn, Produkcja, Bom

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/magazyn')
def magazyn():
    items = Magazyn.query.all()
    return render_template('magazyn.html', items=items)

@app.route('/produkcja')
def produkcja():
    produkcja_items = Produkcja.query.all()
    return render_template('produkcja.html', items=produkcja_items)

@app.route('/bom')
def bom():
    bom_items = Bom.query.all()
    return render_template('bom.html', items=bom_items)

if __name__ == '__main__':
    app.run(debug=True)
