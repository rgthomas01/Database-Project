from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

app = Flask(__name__)

#app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
#app.config['MYSQL_USER'] = 'cs340_thomrach'
#app.config['MYSQL_PASSWORD'] = '####' #last 4 of onid
#app.config['MYSQL_DB'] = 'cs340_thomrach'
#app.config['MYSQL_CURSORCLASS'] = "DictCursor"

db_connection = db.connect_to_database()
mysql = MySQL(app)

# Routes
#homepage
@app.route('/')
def root():
    return render_template("main.html") 

#customers
@app.route('/customers', methods=["POST", "GET"])
def customers():
    if request.method == "POST":
        #if user presses add button 
        if request.form.get("Save"):
        #grab user form inputs
            customerId = request.form["customerId"]
            firstName = request.form["firstName"]
            lastName = request.form["lastName"]
            customerEmail=request.form["customerEmail"]
            membershipStatus = request.form["membershipStatus"]

        return redirect("/customers")
            
         #   query = "INSERT INTO customers (firstName, lastName, customerEmail, membershipStatus) VALUES (%s,%s,%s,%s)"
          #  cur = mysql.connection.cursor()
        # cur.execute(query,(firstName, lastName, customerEmail, membershipStatus))
         #  mysql.connection.commit()
        

    return render_template("/customers/index.j2") 

@app.route('/customers/retrieved', methods=["GET", "POST"])
def customersRetrieved():
    query = "Select * FROM Customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = (cursor.fetchall())
    return render_template("/customers/retrieved.j2", Customers=results) 

@app.route('/customers/update/<int:id>', methods=["GET","POST"])
def update_customers(id):
    #query to grab info of customer with passed id
    if request.method=="GET":
        query = "SELECT * FROM Customers WHERE customerId = %s" %(id)
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = (cursor.fetchall())
        return render_template("/customers/update.j2", Customers=results) 

    if request.method=="POST":
        if request.form.get("Update"):
            # grab user form inputs
            customerId = request.form["customerId"]
            customerFirstName = request.form["customerFirstName"]
            customerLastName= request.form["customerLastName"]
            customerEmail = request.form["customerEmail"]
            membershipStatus = request.form["membershipStatus"]

        query = "UPDATE Customers SET customerFirstName = %s, customerLastName = %s, customerEmail = %s, membershipStatus = %s WHERE customerId =%s"
        test = 'customerFirstName', 'customerLastName', 'customerEmail', 'membershipStatus', 'customerId'
        cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (customerFirstName, customerLastName, customerEmail, membershipStatus, customerId))       
        results = (cursor.fetchall())
        return redirect("/customers/retrieved")




        #if the user clicks the update button 
    
    return redirect('customers.retrieved.j2')


@app.route('/purchases')
def purchases():
    return render_template("purchases.html")

@app.route('/purchases/results') 
def purchase_results():
    return render_template("purchase_results.html")

@app.route('/purchases/results/not_found') 
def purchase_results_not_found():
    return render_template("results_not_found.html") 

@app.route('/purchases/add') 
def add_purchase():
    return render_template("add_purchase.html")

@app.route('/purchases/delete') 
def delete_purchase():
    return render_template("delete_purchase.html")

# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    
    app.run(port=3839, debug=True)