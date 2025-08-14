import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DB_USER','abc')}:{os.getenv('DB_PASSWORD','TwojeHaslo')}"
        f"@{os.getenv('DB_HOST','dpg-d2e5n4ggjchc73e2e6i0-a')}:{os.getenv('DB_PORT','5432')}/{os.getenv('DB_NAME','magazyn_wwo2')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
