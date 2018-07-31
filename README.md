######################## EXAMPLES ###########################################

>>> channel = Channel.query.filter_by(name='pretty printed').first()
>>> channel2 = Channel.query.filter_by(name='Cat videos').first()
>>> users = User.query.all()
>>> users
[<User 1>, <User 2>, <User 3>, <User 4>]
>>> nikhil = users[0]
>>> vishal = users[1
... ]
>>> shail = users[2]
>>> mukesh = users[3]
>>> channel.subscribers(shail)
>>> channel.subscribers.append(nikhil)
>>> db.session.commit()
>>> channel.subscribers.append(vishal)
>>> channel2.subscribers.append(shail)
>>> channel2.subscribers.append(mukesh)
>>> channel.subscibers.append(nikhil)
>>> channel.subscribers.append(mukesh)
>>> db.session.commit()
>>> for user in channel.subscribers:
...     user.name
...
'Nikhil'
'Vishal'


################################## MIGRATIONS ################################
use flask-migrate to do migrations.
use flask-script to make app.py accept command line args.

'db' command is accepted by app.py. This command has init, migrate and upgrade sub commands
which are explained below.

First time:

python app.py db init ---> This will create initial migrations for first time.

After:

python app.py db migrate ---> This will generate files on your system.
python app.py db upgrade ----> This will apply changes from models to actual db.

################################# QUERY PATTERNS ################################

p.owner # The Person object who owns this  pet. See app.py for how models are layed out.
p = Pet.query.filter_by(id=1).first() ---> First instance from Pet table.
all_pets = Pet.query.all() ---> All pets.

#################################### SCHEMA #####################################
use __table_args__ = { 'schema': 'your schema name'} for each model you define
to attach a schema for that model.
use CREATE SCHEMA <name> to first create a schema.

##################### MULTIPLE DATABASES  #######################################

add this config.

app.config['SQLALCHEMY_BINDS'] = {
  '<name of db>': '<path for db>'
}

>>> db.create_all(bind='micky')

####################### CONSTRAINNTS ######################################

name = db.Column(db.String(20), unique=True)
notnull = db.Column(db.String(20), nullable=False)
default = db.Column(db.Integer, server_default=20)
check = db.Column(db.Integer, db.CheckConstraint('check > 5')) # only if check > 5

#################### BULK UPDATE AND BULK DELETE ##########################


>>> from random import choice
>>> choices = ['a', 'b', 'c', 'd']
>>> for i in range(1, 101):
...     a = Data(letter=choice(choices))
...     db.session.add(a)
...
>>> db.session.commit()
>>> a  = Data.query.filter_by(letter='a').all()
>>> len(a)
20
>>> updated  = Data.query.filter_by(letter='a').update({ Data.letter: 'b'})
>>> updated
20
>>> db.session.commit()
>>> a  = Data.query.filter_by(letter='a').all()
>>> len(a)
0
>>> Data.query.filter_by(letter='b').delete()
38
>>>

########################### LAZY ###########################################

how the data for the relationship is loaded ?

lazy = 'select', 'dynamic', 'joined', 'subquery'

'select' / True (which is the default, but explicit is better than implicit) means that SQLAlchemy will load the data as necessary
 in one go using a standard select statement.
'joined' / False tells SQLAlchemy to load the relationship in the same query as the parent using a JOIN statement.
'subquery' works like 'joined' but instead SQLAlchemy will use a subquery.
'dynamic' is special and can be useful if you have many items and always want to apply additional SQL filters to them. Instead of loading the items SQLAlchemy will return another query object which you can further refine before loading the items. Note that this cannot be turned into a different loading strategy when querying so it’s often a good idea to avoid using this in favor of lazy=True. A query object equivalent to a dynamic user.addresses relationship can be created using

#################### LEFT OUTER JOIN ######################################
