from app import db

class Bartender(db.Model):
    __tablename__ = 'bartenders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    hometown = db.Column(db.String(120))
    birthyear = db.Column(db.Integer)