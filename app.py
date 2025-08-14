from flask import Flask, render_template
from config import Config
from models import db, Magazyn, BOM, Produkcja

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/magazyn/view')
def view_magazyn():
    produkty = Magazyn.query.all() or []
    return render_template('magazyn.html', produkty=produkty)

@app.route('/bom/view')
def view_bom():
    bom = BOM.query.all() or []
    return render_template('bom.html', bom=bom)

@app.route('/produkcja/view')
def view_produkcja():
    produkcja = Produkcja.query.all() or []
    return render_template('produkcja.html', produkcja=produkcja)

if __name__ == '__main__':
    app.run(debug=True)
