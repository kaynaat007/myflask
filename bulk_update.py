from app import db


class Data(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    letter = db.Column(db.String(20))
    
