import string
from datetime import datetime
from random import choices

from .extensions import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True) # ID created automatically by the database
    original_url = db.Column(db.String(512)) # this is what we are passing in
    short_url = db.Column(db.String(3), unique=True) # will be generated in dunder init 
    visits = db.Column(db.Integer, default=0) # defaults to 0
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link() # short URL generated here

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=4)) # K length 

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()

        return short_url
