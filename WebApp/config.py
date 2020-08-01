import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(DIR_PATH, os.pardir))


class Config:

    SECRET_KEY = "secret"
    PORT_NUMBER = 5000
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{ROOT_PATH}/site.db"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@host/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
