import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = os.getenv('DEBUG') == 'True'
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    
    MAIL_SERVER = os.getenv('MAIL_SERVER')

    MAIL_PORT = int(os.getenv('MAIL_PORT'))

    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS') == 'True'

    MAIL_USERNAME = os.getenv('MAIL_USERNAME')

    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')