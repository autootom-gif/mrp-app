import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://abc:xruiiXquETHElmravuoxAXv5wUMuzs2l@dpg-d2e5n4ggjchc73e2e6i0-a:5432/magazyn_wwo2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
