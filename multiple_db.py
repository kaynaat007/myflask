from app  import db, app

app.config['SQLALCHEMY_BINDS'] = {
   'micky' : 'postgres://postgres:postgres@localhost:5432/micky'
}  

class One(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Two(db.Model):
    __bind_key__ = 'micky'
    id = db.Column(db.Integer, primary_key=True)

class Three(db.Model):
    __bind_key__ = 'micky'
    id = db.Column(db.Integer, primary_key=True)
