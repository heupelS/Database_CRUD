#app.py
import re
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
from turtle import title
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "dbs_2022" #Minhs passwort
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

def create_figure(data):
    
    fig = Figure()    
    axis = fig.add_subplot(1, 1, 1)
    axis.set_ylabel("Article count")
    axis.grid()
    
    data.groupby('year').size().plot(kind = 'bar',ax=axis)

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String = pngImageB64String + base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String
 
@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM articles"
    cur.execute(s) # Execute the SQL
    list_articles = cur.fetchall()
    data = pd.read_sql_query(s, conn)
    image = create_figure(data)
    return render_template('index.html', list_articles = list_articles, image=image)
 
@app.route('/add_article', methods=['POST'])
def add_article():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']
        journal = request.form['journal']
        h_index = request.form['h_index']
        refperdoc = request.form['refperdoc']
        cur.execute("INSERT INTO articles (id, author, title, year, journal, h_index, refperdoc) VALUES ((SELECT MAX(id)+1 FROM public.articles),%s,%s,%s,%s,%s,%s)", (author,title,year,journal,h_index,refperdoc))
        conn.commit()
        flash('article added')
        return redirect(url_for('Index'))
 
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_article(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM articles WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', article = data[0])
 
@app.route('/update/<id>', methods=['POST'])
def update_article(id):
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']
        journal = request.form['journal']
        h_index = request.form['h_index']
        refperdoc = request.form['refperdoc']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE articles
            SET author = %s,
                title = %s,
                year = %s,
                journal = %s,
                h_index = %s,
                refperdoc = %s                
            WHERE id = %s
        """, (author,title,year,journal,h_index,refperdoc,id))
        flash('article updated')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_article(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM articles WHERE id = {0}'.format(id))
    conn.commit()
    flash('article deleted')
    return redirect(url_for('Index'))
 
if __name__ == "__main__":
    app.run(debug=True)