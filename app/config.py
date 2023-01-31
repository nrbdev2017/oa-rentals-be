from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql+psycopg2://admin:a13@127.0.0.1/oarentals'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LANGUAGES = ['en', 'sw']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    TOKEN_EXPIRY_SECONDS = 600000
