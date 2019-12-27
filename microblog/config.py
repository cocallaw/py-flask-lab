import os
import urllib.parse
basedir = os.path.abspath(os.path.dirname(__file__))

params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=pyclc.database.windows.net;DATABASE=pyflask;UID=FlaskApp01@sqldb;PWD=P@ssword1!")

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_TRACK_MODIFICATIONS = False