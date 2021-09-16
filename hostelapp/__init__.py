#This file will import all the things we need in this package so that it #will be assessible to any module in the package, any module can import as #from thispackage import xx '''

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from hostelapp.api import apiobj

from hostelapp.site import siteobj

def create_app():
    app=Flask(__name__,instance_relative_config=True)
    from hostelapp import config
    #app.config.from_object(config.LiveConfig)
    app.config.from_pyfile('config.py')
    from hostelapp.mymodel import db
    db=SQLAlchemy()
    db.init_app(app)
    app.register_blueprint(apiobj)
    app.register_blueprint(siteobj)
    return app

def create_db():
    from hostelapp.mymodel import db 
    app = create_app()
    with app.app_context():
        db.create_all()

#csrf = CSRFProtect()  #or use this method csrf.init_app(app)

#load the package's config here after the app has been created

# from hostelapp import config #config within package folder
# app.config.from_object(config.LiveConfig)
# app.config.from_pyfile('config.py') #loads config from instance folder

# No need to load routes here anymore, they are being loaded in the respective blueprint's init
# from projectapp import myroutes
from hostelapp import forms
from hostelapp import mymodel