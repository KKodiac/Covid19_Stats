import sqlite3 as sql
from flask import g
from db_setting import *


# DB INIT
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# get_db().cursor() inits DB
def get_db():
    db = getattr(g, '_database', None)
    if(db == None):
        db = g._database = sql.connect(DATABASE)

    db.row_factory = sqlite3.Row
    return db, db.row_factory, db.co

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    cursor = get_db().cursor()
    return cursor

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
