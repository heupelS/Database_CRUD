import sqlite3
import os
from flask import g, Flask
from flask import render_template
from flask import request

import psycopg2
        
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/list')
    def books():
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT * FROM books;')
        books = cur.fetchall()
        cur.close()
        conn.close()
        print(books)
        return render_template("books.html", books=books)
    
    @app.route('/')
    def my_form():
        return render_template('form.html')
    
    @app.route('/', methods=['POST'])
    def my_form_post():
        text = request.form['text']
        print("QUERY: " + text)
        cur = get_db().cursor()
        entryList = []
        for entry in query_db(text):
            entryList.append(entry)
        processed_text = text.upper()
        return render_template('form.html', list=entryList)
        
    return app
    
    

DATABASE = "C:\\Users\\Mister Sandman\\Desktop\\Uni\\DBS\\u10_Kern_Nguyen_Heupel\\Merged.db" 

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def get_db():
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='postgres',
        password='13071996')

    return conn


def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
app = create_app()
app.run(debug=True)