from flask import Blueprint, render_template, request, redirect
from .extensions import db

from .models import Link

# Request object - needed for servers's response to HTTP request


 
short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404() # https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

    link.visits = link.visits + 1
    db.session.commit()
    return redirect(link.original_url)  

@short.route('/')
def index():
    return render_template('s.html')

@short.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()
    #request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
    
    return render_template('link_added.html', 
        new_link=link.short_url, original_url=link.original_url)

@short.route('/stats') 
def stats():
    links = Link.query.all()

    return render_template('stats.html', links=links)


@short.errorhandler(404)
def page_not_found(e):
    #return '<h1>404</h1>', 404 
    return render_template('4004.html'), 404