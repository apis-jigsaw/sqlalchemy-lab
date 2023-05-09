from app import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    city = db.Column(db.String(120))
    category = db.Column(db.String(120))
    rating = db.Column(db.Float())
    url = db.Column(db.String(120))