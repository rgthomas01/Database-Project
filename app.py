from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_thomrach'
app.config['MYSQL_PASSWORD'] = '9244' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_thomrach'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

db_connection = db.connect_to_database()
mysql = MySQL(app)

# Routes
@app.route('/')
def root():
    return render_template("main.j2") 

@app.route('/customers')
def customers():
    query = "Select * FROM Customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = (cursor.fetchall())
    return render_template("customers.j2", Customers=results) 


@app.route('/purchases')
def purchases():
    return "This is the purchases route"


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    
    app.run(port=3838, debug=True)