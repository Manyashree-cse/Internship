# class Config:
#     SECRET_KEY = 'secretkey'
    
#     SQLALCHEMY_DATABASE_URI = \
#     'mysql+pymysql://journal_user:password@localhost/journal_db'

#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     UPLOAD_FOLDER = 'static/uploads'
#     GEMINI_API_KEY = "AIzaSyComPD92WP72ulTAgdZCrMsKhH_DgEAXKg"

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')

    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')    