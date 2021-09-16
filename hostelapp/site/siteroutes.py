from operator import concat
from flask import render_template, make_response,flash,url_for, redirect, sessions
from werkzeug.wrappers import request
from sqlalchemy import desc

from flask import render_template,url_for,session

#import the blueprint's instance
from . import siteobj

@siteobj.route('/')
def home(): 
    return "Welcome to Home Page"

@siteobj.route('/about-me/life')
def about(): 
    return render_template('about.html')