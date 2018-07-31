from app  import db


class MyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class MySecondTable(db.Model):
    __table_args__ = {'schema': 'myschema' }
    id = db.Column(db.Integer, primary_key=True)

class Pet(db.Model):
    __table_args__ = { 'schema': 'myschema'} # define schema here. create first with CRETAE SCHEMA <schema name> statement.
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
