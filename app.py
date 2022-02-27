from flask import Flask, render_template, json, redirect, request #added request
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db
import json

app = Flask(__name__)

# ------------------------------SQL CONNECTION------------------------------

# app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
# app.config['MYSQL_USER'] = 'cs340_bushjam'
# app.config['MYSQL_PASSWORD'] = '####' #last 4 of onid
# app.config['MYSQL_DB'] = 'cs340_bushjam'
# app.config['MYSQL_CURSORCLASS'] = "DictCursor"


db_connection = db.connect_to_database()
mysql = MySQL(app)

# ------------------------------DATA------------------------------

with open('data/mockData.json', 'r+') as infile:
    mockData = json.load(infile)



# ------------------------------MAIN------------------------------

@app.route('/',methods=["GET"])
def main():
    if request.method == "GET": 
            return render_template("main.j2")

# ------------------------------RETRIEVE------------------------------

def retrieve(dbEntity, data):
    # RETRIEVE - landing page / retrieve results 
    if request.method == "GET": 

        # Landing page for search - take non-query URL request to /<dbEntity>
        if len(request.args) == 0:
            return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False, data=None)

        # Retrieval page - take query URL to /<dbEntity> and render table template with matching data
        elif len(request.args) > 0:
            return render_template("retrieve.j2", dbEntity=dbEntity, search=True, created=False, data=data)
    

@app.route('/employees',methods=["GET", "POST"])
def employeeRetrieve():

    dbEntity = "employees"

    if request.method == "GET":
        query = "Select * FROM Employees;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = (cursor.fetchall())
        return retrieve(dbEntity, data= results)


@app.route('/customers',methods=["GET", "POST"])
def customerRetrieve():
    dbEntity = "customers"

    if request.method == "GET":
        query = "Select * FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = (cursor.fetchall())
        return retrieve(dbEntity, data=results)
    


@app.route('/purchases',methods=["GET", "POST"])
def purchasesRetrieve():

    dbEntity = "purchases"

    if request.method == "GET":
        query = "Select * FROM Purchases;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = (cursor.fetchall())
        return retrieve(dbEntity, data=results)

@app.route('/items',methods=["GET", "POST"])
def itemsRetrieve():

    dbEntity = "items"

    if request.method == "GET":
        query = "Select * FROM Items;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = (cursor.fetchall())
        return retrieve(dbEntity, data= results)


# ------------------------------CREATE------------------------------

def create(dbEntity, formPrefillData=None):
    """ Create and confirm new entry in database table.  

    Keyword arguments: 
        dbEntity -- corresponds to table in the databae, e.g., Employees
        formPrefill -- to pre-populate UI form with existing database values, e.g., eeIds, customerIds
    """

   # Blank form to create 
    if request.method == "GET":
         return render_template("createUpdate.j2", dbEntity=dbEntity, formPrefillData=formPrefillData, operation="create", created=False)

    # Submit created dbEntity
    elif request.method == "POST":
        # The request.form object a Werkzeug dict, can be accessed like a dict with .keys(), .items(), .values(): 
        # See: https://tedboy.github.io/flask/generated/generated/werkzeug.MultiDict.listvalues.html#werkzeug.MultiDict.listvalues
    
        return render_template("createUpdate.j2", dbEntity=dbEntity, formPrefillData=formPrefillData, data=dict(request.form.items()), operation="create", created=True) 


@app.route('/employees/create',methods=["GET", "POST"])
def employeesCreate():

    dbEntity = "employees"
    if request.method == "POST":
        eeFirstName = request.form["eeFirstName"]
        eeLastName= request.form["eeLastName"]
        eePosition = request.form["eePosition"]

        query = "INSERT INTO Employees (eeId, eeFirstName, eeLastName,eePosition) VALUES (NULL, %s,%s,%s);"
        cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (eeFirstName,eeLastName, eePosition, ))       
        results = (cursor.fetchall())

    return create(dbEntity)

@app.route('/customers/create',methods=["GET", "POST"])
def customersCreate():

    dbEntity = "customers"
    if request.method == "POST":
        customerFirstName = request.form["customerFirstName"]
        customerLastName= request.form["customerLastName"]
        customerEmail = request.form["customerEmail"]
        membershipStatus = request.form["membershipStatus"]

        #if customerEmail is null 
        if customerEmail == "":
            query = "INSERT INTO Customers (customerId, customerFirstName, customerLastName, membershipStatus) VALUES (NULL, %s,%s,%s);"
            cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (customerFirstName, customerLastName, membershipStatus, ))       
            results = (cursor.fetchall())
        
        #if all values are provided 
        else:
            query = "INSERT INTO Customers (customerId, customerFirstName, customerLastName, customerEmail, membershipStatus) VALUES (NULL, %s,%s,%s,%s);"
            cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (customerFirstName, customerLastName, customerEmail, membershipStatus, ))       
            results = (cursor.fetchall())

    return create(dbEntity)



@app.route('/purchases/create',methods=["GET", "POST"])
def purchasesCreate():

    dbEntity = "purchases"

    # Get eeId and customerId data to populate formPrefillData
    if request.method == "GET":
        formPrefillData = {'eeIds':[],'customerIds':[]}
        # Get eeId values 
        query = "SELECT eeId FROM Employees;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        formPrefillData['eeIds'] = cursor.fetchall()
        # Get customerId values 
        query = "SELECT customerId FROM Customers;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        formPrefillData['customerIds'] = cursor.fetchall()

        return create(dbEntity, formPrefillData)


    if request.method == "POST":
        purchaseDate = request.form["purchaseDate"]
        customerId= request.form["customerId"]
        eeId = request.form["eeId"]
        creditCardNumb = request.form["creditCardNumb"]
        creditCardExp = request.form["creditCardExp"]
        costOfSale = request.form["costOfSale"]
        

        #if self checkout was used. EmployeeId is NULL
        if eeId =="":
            query = "INSERT INTO Purchases (purchaseId, customerId, purchaseDate, creditCardNumb, creditCardExp, costOfSale) VALUES (NULL, %s,%s,%s,%s,%s);"
            cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (customerId, purchaseDate, creditCardNumb, creditCardExp, costOfSale ))       
            results = (cursor.fetchall())

        else:    
            query = "INSERT INTO Purchases (purchaseId, customerId, purchaseDate, creditCardNumb, creditCardExp, costOfSale, eeId) VALUES (NULL, %s,%s,%s,%s,%s,%s);"
            cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (customerId, purchaseDate, creditCardNumb, creditCardExp, costOfSale    , eeId, ))       
            results = (cursor.fetchall())
        
        #take purchaseId from purchase record created to use in adding PurchaseItems
        cursor.execute('select LAST_INSERT_ID()')
        purchaseIdtuple = (cursor.fetchall())
        purchaseId = purchaseIdtuple[0].get('LAST_INSERT_ID()')
        
       #TODOS ->
        #select last_insert may not be way to go here, need to look at functionality may be better to get purchaseId through a select.
        #https://dba.stackexchange.com/questions/81604/how-to-insert-values-in-junction-table-for-many-to-many-relationships
       
        
        # Loop through >= 1 itemId and itemQuantity values from form, insert into PurchaseItems 
        # TODO add support to check Item quantity prior to completing purchase 
        purchaseItemIds = [request.form[i] for i in request.form.keys() if 'itemId' in i]
        purchaseItemQuantities = [request.form[i] for i in request.form.keys() if 'itemQuantity' in i]
        for i in range(len(purchaseItemIds)):
            query = "INSERT INTO PurchaseItems (purchaseId, itemId, itemQuantity) VALUES (%s,%s,%s);"
            cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (purchaseId, purchaseItemIds[i], purchaseItemQuantities[i]))       
            results = (cursor.fetchall())

        return create(dbEntity)


@app.route('/items/create',methods=["GET", "POST"])
def itemsCreate():
    

    dbEntity = "items"
    if request.method == "POST":
        itemName = request.form["itemName"]
        itemPrice= request.form["itemPrice"]
        itemDescription = request.form["itemDescription"]
        itemType = request.form["itemType"]
        inventoryOnHand = request.form["inventoryOnHand"]


        query = "INSERT INTO Items (itemId, itemName, itemPrice, itemDescription, itemType, inventoryOnHand) VALUES (NULL,%s,%s,%s,%s,%s);"
        cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (itemName, itemPrice, itemDescription, itemType, inventoryOnHand, ))       
        results = (cursor.fetchall())

    return create(dbEntity)


# ------------------------------UPDATE------------------------------

def update(dbEntity, data):

    if request.method == "GET":
        # Parse incoming request to get id attribute name (e.g., 'eeId', 'purchaseId') and its value
        updateRecord = [i for i in request.args.items()]
        entityId = updateRecord[0][0]
        idValue = updateRecord[0][1]

        # Locate the subject in the db by id, assign subject's information (dict()) to updateRecord
        for i in data:
            if i[entityId] == idValue:
                updateRecord = i

        # Pull existing items for purchases update
        if dbEntity == "purchases":
            existingItems = mockData['purchasesItems']
        else: 
            existingItems = []

        # Render the template, pre-populated with subject's existing information from db
        return render_template("createUpdate.j2", dbEntity=dbEntity, data=data, operation="update", updateRecord=updateRecord, existingItems=existingItems, updated=False)

    # Submit new information to affect update 
    if request.method == "POST":
        print(request.form)
        # Can probably get rid of updated=True/False
        return render_template("createUpdate.j2", dbEntity=dbEntity, data=dict(request.form.items()), operation="update",updateRecord=None, updated=True)


@app.route('/employees/update',methods=["GET", "POST"])
def employeesUpdate():

    dbEntity = "employees"
    data = mockData['employees']

    return update(dbEntity, data)
 

@app.route('/customers/update',methods=["GET", "POST"])
def customersUpdate():

    dbEntity = "customers"
    data = mockData['customers']

    return update(dbEntity, data)
    


@app.route('/purchases/update',methods=["GET", "POST"])
def purchasesUpdate():

    dbEntity = "purchases"
    data = mockData['purchases']

    return update(dbEntity, data)


@app.route('/items/update',methods=["GET", "POST"])
def itemsUpdate():

    dbEntity = "items"
    data = mockData['items']

    return update(dbEntity, data)


# ------------------------------DELETE------------------------------

def delete(dbEntity,data):
        
    if request.method == "GET":
        # Parse incoming request to get id attribute name (e.g., 'eeId', 'purchaseId') and its value

        entityId = deleteRecord[0][0]
        idValue = deleteRecord[0][1]

        query= "SELECT * FROM " + dbEntity.title() + " WHERE " + entityId+ " = %s" 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idValue, ))       
        deleteRecord = (cursor.fetchall())
        

        # Render the template, pre-populated with subject's existing information from db
        return render_template("delete.j2", dbEntity=dbEntity, data=data, operation="delete", deleteRecord=deleteRecord, deleted=False)
  
    # Submit new information to affect delete 
    if request.method == "POST":
        eeId=(request.form['confirmDelete'])

        query = "SELECT * FROM Employees WHERE eeId = %s " 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(eeId, ))       
        deleteRecord = (cursor.fetchall())

        #Still need to run actual delete query. Convert select to dict to populated sucessfuly deleted from 
        #Then run delete query
        #https://stackoverflow.com/questions/28755505/how-to-convert-sql-query-results-into-a-python-dictionary



        # Can probably get rid of deleted=True/False
        return render_template("delete.j2", dbEntity=dbEntity, data=(deleteRecord), operation="delete",deleteRecord=deleteRecord, deleted=True) 


@app.route('/employees/delete',methods=["GET", "POST"])
def employeesDelete():

    dbEntity = "employees"

    if request.method == "GET":
        eeId = request.args['eeId']
        
        
        query = "SELECT * FROM Employees WHERE eeId = %s " 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(eeId, ))       
        data = (cursor.fetchall())


    #data = mockData['employees']

        return delete(dbEntity, data)
    
    if request.method == "POST":
        confirmDelete= request.form
        data =(confirmDelete.getlist('confirmDelete'))
        
        
        return delete(dbEntity, data)




@app.route('/customers/delete',methods=["GET", "POST"])
def customersDelete():

    dbEntity = "customers"
    data = mockData['customers']

    return delete(dbEntity, data)


@app.route('/purchases/delete',methods=["GET", "POST"])
def purchasesDelete():

    dbEntity = "purchases"
    data = mockData['purchases']

    return delete(dbEntity, data)


@app.route('/items/delete',methods=["GET", "POST"])
def itemsDelete():

    dbEntity = "items"
    data = mockData['items']

    return delete(dbEntity, data)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3838))
    app.run(host='localhost.',port=port, debug=True)