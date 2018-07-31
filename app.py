from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://root:root@localhost:5432/tutorial'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner' ) # psesudo column


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id')) # actual column
    gender = db.Column(db.String(20))


if __name__ == '__main__':
    manager.run()
