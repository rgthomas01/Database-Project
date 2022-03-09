from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db
import itertools

app = Flask(__name__)

# ------------------------------SQL CONNECTION------------------------------

mysql = MySQL(app)

# ------------------------------MAIN------------------------------

@app.route('/',methods=["GET"])
def main():
    db_connection = db.connect_to_database()
    if request.method == "GET": 
            return render_template("main.j2")

# ------------------------------RETRIEVE------------------------------

def retrieve(dbEntity, data=None):
    #test comment for branching 2
    # RETRIEVE - landing page / retrieve results
    db_connection = db.connect_to_database() 
    if request.method == "GET": 

        # Landing page for search - take non-query URL request to /<dbEntity>
        if len(request.args) == 0:
            return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False)

        # Retrieval page - take query URL to /<dbEntity> and render table template with matching data
        elif len(request.args) > 0:
            return render_template("retrieve.j2", dbEntity=dbEntity, search=True, created=False, data=data)
    

@app.route('/employees',methods=["GET", "POST"])
def employeeRetrieve():
    db_connection = db.connect_to_database()
    dbEntity = "employees"

    #get arguements from Get Request
    retrieveRecord = [i for i in request.args.items()]


    if request.method == "GET" and len(retrieveRecord)>=1:
        
        if 'retrieveAll' in request.args.keys(): #if retrieve all 
        
            query = "Select * FROM Employees;"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = (cursor.fetchall())

            if len(results) == 0: #if db is empty 
               results = None
            return retrieve(dbEntity, data=results)

        else:
            paramList = []
            
            #catch non empty params and add them to a paramList to be used as query_params
            if request.args['eeId'] != '':
                eeId = request.args['eeId']
                paramList.append(eeId)
            if request.args["eeFirstName"] != '':
                eeFirstName = request.args['eeFirstName']
                paramList.append(eeFirstName)
            if request.args['eeLastName'] != '':
                eeLastName = request.args['eeLastName']
                paramList.append(eeLastName)
            if request.args['eeStatus'] != '':
                eeStatus = request.args['eeStatus']
                paramList.append(eeStatus)


            #build string to use after WHERE clause
            selectStr = ''
            for i in request.args.keys():
                if request.args[i] != '':
                    
                    if len(selectStr)>0:
                        selectStr = selectStr +" AND "
                    selectStr = selectStr + i + " = %s"

            if len(selectStr)== 0:      # if blank search 
                return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False)

            else:
                query =  "Select * FROM Employees WHERE " + selectStr +";   " 
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params = tuple(paramList, ))
                results = (cursor.fetchall())

                if len(results) ==0:
                    results = None

            return retrieve(dbEntity, data=results)


    else:
        return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False)


@app.route('/customers',methods=["GET", "POST"])
def customerRetrieve():
    db_connection = db.connect_to_database()
    dbEntity = "customers"

    #get arguements from Get Request
    retrieveRecord = [i for i in request.args.items()]

    if request.method == "GET" and len(retrieveRecord)>=1:
        
        if 'retrieveAll' in request.args.keys(): #if retrieve all 
            query = "Select * FROM Customers;"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = (cursor.fetchall())
            
            if len(results) == 0: #if db is empty 
               results = None

            return retrieve(dbEntity, data=results)
        
        else:
            paramList = []
            
            #catch non empty params and add them to a paramList to be used as query_params
            if request.args['customerId'] != '':
                customerId = request.args['customerId']
                paramList.append(customerId)
            if request.args["customerFirstName"] != '':
                customerFirstName = request.args['customerFirstName']
                paramList.append(customerFirstName)
            if request.args['customerLastName'] != '':
                customerLastName = request.args['customerLastName']
                paramList.append(customerLastName)
            if request.args['customerEmail'] != '':
                customerEmail = request.args['customerEmail']
                paramList.append(customerEmail)

            #build string to use after WHERE clause
            selectStr = ''
            for i in request.args.keys():
                if request.args[i] != '':
                    
                    if len(selectStr)>0:
                        selectStr = selectStr +" OR "
                    selectStr = selectStr + i + " = %s"

            if len(selectStr)== 0:      # if blank search 
                return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False)

            else:
                query =  "Select * FROM Customers WHERE " + selectStr +  ";" 
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params = tuple(paramList, ))
                results = (cursor.fetchall())
                
                if len(results)==0:
                    results = None
                    
            return retrieve(dbEntity, data=results)

        
    else:
       return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False)


@app.route('/purchases',methods=["GET", "POST"])
def purchasesRetrieve():
    db_connection = db.connect_to_database()

    dbEntity = "purchases"

    retrieveRecord = [i for i in request.args.items()]

    if request.method == "GET" and len(retrieveRecord)>=1 :
        
        
        if 'retrieveAll' in request.args.keys(): #if retrieve all 
            query = "Select * FROM Purchases;"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = (cursor.fetchall())

            if len(results) == 0: #if db is empty 
               results = None
            
            return retrieve(dbEntity, data=results)
        
        else:
            paramList = []
    

            #catch non empty params and add them to a paramList to be used as query_params
            if request.args['purchaseDate'] != '':
                purchaseDate = request.args['purchaseDate']
                paramList.append(purchaseDate)
            if request.args["purchaseId"] != '':
                purchaseId = request.args['purchaseId']
                paramList.append(purchaseId)
            if request.args['customerId'] != '':
                customerId = request.args['customerId']
                paramList.append(customerId)
            if request.args['eeId'] != '':
                eeId = request.args['eeId']
                paramList.append(eeId)

            #build string to use after WHERE clause
            selectStr = ''
            for i in request.args.keys():
                if request.args[i] != '':
                    
                    if len(selectStr)>0:
                        selectStr = selectStr +" OR "
                    selectStr = selectStr + i + " = %s"
                
            if len(selectStr)==0:      # if blank search 
                return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False)

            else:
                query =  "Select * FROM Purchases WHERE " + selectStr +  ";" 
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params = tuple(paramList, ))
                results = (cursor.fetchall())
            
                if len(results)==0: 
                    results = None

            return retrieve(dbEntity, data=results)

        
    else:
        return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False)

@app.route('/items',methods=["GET", "POST"])
def itemsRetrieve():
    db_connection = db.connect_to_database()
    dbEntity = "items"

    retrieveRecord = [i for i in request.args.items()]

    if request.method == "GET" and len(retrieveRecord)>0:
        
        if 'retrieveAll' in request.args.keys(): #if retrieve all 
            query = "Select * FROM Items;"
            cursor = db.execute_query(db_connection=db_connection, query=query)
            results = (cursor.fetchall())
            return retrieve(dbEntity, data=results)

            if len(results) == 0: #if db is empty 
               results = None
        
        else:
            paramList = []
    

            #catch non empty params and add them to a paramList to be used as query_params
            if request.args['itemId'] != '':
                itemId = request.args['itemId']
                paramList.append(itemId)
            if request.args["itemName"] != '':
                itemName = request.args['itemName']
                paramList.append(itemName)
            if request.args['itemPrice'] != '':
                itemPrice = request.args['itemPrice']
                paramList.append(itemPrice)
            if request.args['itemType'] != '':
                itemType = request.args['itemType']
                paramList.append(itemType)

            #build string to use after WHERE clause
            selectStr = ''
            for i in request.args.keys():
                if request.args[i] != '':
                    
                    if len(selectStr)>0:
                        selectStr = selectStr +" OR "
                    selectStr = selectStr + i + " = %s"

            if len(selectStr)== 0:      # if blank search 
                return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False)

            else:
                query =  "Select * FROM Items WHERE " + selectStr +  ";" 
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params = tuple(paramList, ))
                results = (cursor.fetchall())
            
                if len(results)==0:
                    results = None

                return retrieve(dbEntity, data=results)

        
    else:
        return render_template("retrieve.j2",dbEntity=dbEntity, search=False, created=False)

# ------------------------------CREATE------------------------------

def create(dbEntity, formPrefillData=None):
    """ Create and confirm new entry in database table.  

    Keyword arguments: 
        dbEntity -- corresponds to table in the databae, e.g., Employees
        formPrefill -- to pre-populate UI form with existing database values, e.g., eeIds, customerIds
    """
    db_connection = db.connect_to_database()

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
    db_connection = db.connect_to_database()

    dbEntity = "employees"
    if request.method == "POST":
        eeFirstName = request.form["eeFirstName"]
        eeLastName= request.form["eeLastName"]
        eePosition = request.form["eePosition"]
        eeStatus = request.form["eeStatus"]

        query = "INSERT INTO Employees (eeId, eeFirstName, eeLastName,eePosition,eeStatus) VALUES (NULL, %s,%s,%s,%s);"
        cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (eeFirstName,eeLastName, eePosition, eeStatus ))       
        results = (cursor.fetchall())

    return create(dbEntity)

@app.route('/customers/create',methods=["GET", "POST"])
def customersCreate():
    db_connection = db.connect_to_database()

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
    db_connection = db.connect_to_database()

    dbEntity = "purchases"

    # formPrefilData is passed to the template
    formPrefillData = {'eeIds':[],'customerIds':[]}
    # Get eeId values 
    query = "SELECT eeId FROM Employees;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    formPrefillData['eeIds'] = cursor.fetchall()
    # Get customerId values 
    query = "SELECT customerId FROM Customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    formPrefillData['customerIds'] = cursor.fetchall()
    # Get itemId, inventoryOnHand values 
    query = "SELECT itemId, inventoryOnHand FROM Items;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    # {{formPrefillData['inventoryItems']}} to access a dict of key:val pairs: {itemIds:inventoryOnHand}
    # pass those through when the template calls addItems.js
    formPrefillData['inventoryItems'] = { str(i['itemId']):int(i['inventoryOnHand']) for i in cursor.fetchall()} #list > template > js array


    # Get eeId and customerId data to populate formPrefillData
    if request.method == "GET":


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
               
       #TODOS ->
        #select last_insert may not be way to go here, need to look at functionality may be better to get purchaseId through a select.
        #https://dba.stackexchange.com/questions/81604/how-to-insert-values-in-junction-table-for-many-to-many-relationships
       
        
        # Update PurchaseItems - Loop through >= 1 itemId and itemQuantity values from form, insert into PurchaseItems 
        # TODO add support to check Item quantity prior to completing purchase 
        #take purchaseId from purchase record created to use in adding PurchaseItems
        cursor.execute('select LAST_INSERT_ID()')
        purchaseId = (cursor.fetchall())[0].get('LAST_INSERT_ID()')
        purchaseItemIds = [request.form[i] for i in request.form.keys() if 'itemId' in i]
        purchaseItemQuantities = [request.form[i] for i in request.form.keys() if 'itemQuantity' in i]
        for i in range(len(purchaseItemIds)):
            query = "INSERT INTO PurchaseItems (purchaseId, itemId, itemQuantity) VALUES (%s,%s,%s);"
            cursor = db.execute_query(db_connection=db_connection, query=query,  query_params = (purchaseId, purchaseItemIds[i], purchaseItemQuantities[i]))       
            results = (cursor.fetchall())
            # adjust Items.inventoryOnHand
            updateInventoryQuery = "UPDATE Items SET inventoryOnHand=inventoryOnHand-%s WHERE itemId=%s;" 
            cursor = db.execute_query(db_connection=db_connection, query=updateInventoryQuery, query_params=(int(purchaseItemQuantities[i]), purchaseItemIds[i],))

        # print(formPrefillData)
        return create(dbEntity, formPrefillData)


@app.route('/items/create',methods=["GET", "POST"])
def itemsCreate():
    db_connection = db.connect_to_database()


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

def update(dbEntity, data=None, formPrefillData=None):
    db_connection = db.connect_to_database()
    # GET will initially show a form filled with existing data. 
    if request.method == "GET":
        # Parse incoming request to get the key:value of dbEntity id (e.g., 'eeId':'123', 'purchaseId':'456')
        updateRecord = [i for i in request.args.items()] # initially holds entityId and idValue 
        entityId = updateRecord[0][0]
        idValue = updateRecord[0][1]

        # Locate the dbEntity entry by its id, assign its data to updateRecord
        query = "SELECT * FROM " + dbEntity.title() + " WHERE " + entityId+ " = %s" # TODO - this needs to be fixed?
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idValue, ))       
        results = (cursor.fetchall())
        updateRecord = list(results)[0]

        # Specific to Purchases, pull associated PurchaseItems
        existingItems = [] # Default if dbEntity not Purchases
        if dbEntity == "purchases":
            # # SQL Version 
            query = "SELECT PurchaseItems.itemId, PurchaseItems.itemQuantity FROM PurchaseItems JOIN Purchases ON Purchases.purchaseId = PurchaseItems.purchaseId WHERE Purchases.purchaseId = %s;"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idValue,))
            results = cursor.fetchall()
            existingItems = list(results)

        # Render the template, pre-populated with subject's existing information from db
        return render_template("createUpdate.j2", dbEntity=dbEntity, data=data, operation="update", updateRecord=updateRecord, existingItems=existingItems, formPrefillData=formPrefillData, updated=False)

    # Submit new information to affect update 
    if request.method == "POST":
        updateRecord = [i for i in request.form.items()]
        entityId = updateRecord[0][0]
        idValue = updateRecord[0][1]

        # Run UPDATE query 
        colVals = dict(request.form.items())
        updateStr = ""
        for key, val in colVals.items():
 
            # For Purchases - update PurchaseItems and Items.inventoryOnHand per itemId and itemQuantity
            if dbEntity == "purchases" and 'item' in str(key):
                # Get itemId per item
                if  'itemId' in str(key):
                    itemId = str(val)
                # Get itemQuantity per item 
                elif 'itemQuantity'in str(key):
                    itemQuantity = str(val)

                    # Query PurchaseItems to see if Item was an existing PurchaseItem in Purchase
                    purchaseItemsQuery = "SELECT * FROM PurchaseItems WHERE (purchaseId,itemId) = (%s,%s);"
                    cursor = db.execute_query(db_connection=db_connection, query=purchaseItemsQuery, query_params=(idValue, itemId,))
                    results = cursor.fetchall()

                    # Item was an EXISTING PurchaseItem on the Purchase
                    if len(results) > 0: 
                        # Difference between new quantity and old
                        itemInventoryChange = int(results[0]['itemQuantity']) - int(itemQuantity)
                        # Update Items.inventoryOnHand if there is an inventory change 
                        if itemInventoryChange != 0:
                            updateInventoryQuery = "UPDATE Items SET inventoryOnHand=inventoryOnHand+%s WHERE itemId=%s;" 
                            cursor = db.execute_query(db_connection=db_connection, query=updateInventoryQuery, query_params=(itemInventoryChange, itemId,))
                            # Update PurchaseItems as well 
                            # If the change to itemQuantity would make the itemQuantity 0, DELETE item from the PurchaseItems
                            if int(results[0]['itemQuantity'])-itemInventoryChange == 0:
                                deltePurchaseItemQuery = "DELETE FROM PurchaseItems WHERE (purchaseId,itemId) = (%s,%s);"
                                cursor = db.execute_query(db_connection=db_connection, query=deltePurchaseItemQuery, query_params=(idValue, itemId,))
                            # Otherwise, just update PurchaseItems.itemQuantity
                            else:
                                updatePurchaseItemsQuery = "UPDATE PurchaseItems SET itemQuantity=itemQuantity-%s WHERE (purchaseId,itemId) = (%s,%s);" 
                                cursor = db.execute_query(db_connection=db_connection, query=updatePurchaseItemsQuery, query_params=(itemInventoryChange,idValue, itemId,))

                    # Item is a NEW PurchaseItem on the Purchase
                    else: 
                        # Update Items.inventoryOnHand if specified itemQuantity is not 0:
                        if int(itemQuantity) > 0: 
                            updateInventoryQuery = "UPDATE Items SET inventoryOnHand=inventoryOnHand-%s WHERE itemId=%s;" 
                            cursor = db.execute_query(db_connection=db_connection, query=updateInventoryQuery, query_params=(int(itemQuantity), itemId,))
                            #Update PurchaseItems.itemQuantity
                            updatePurchaseItemsQuery = "INSERT INTO PurchaseItems (purchaseId,itemId,itemQuantity) VALUES (%s,%s,%s);" 
                            cursor = db.execute_query(db_connection=db_connection, query=updatePurchaseItemsQuery, query_params=(idValue,itemId,itemQuantity,))

            # All other NON-Purcahse entities, compile parameterized query string for update
            else:
                updateStr += (f"{str(key)}='{str(val)}', ")
        
        # Update all other info 
        updateStr = updateStr[:-2]
        query = "UPDATE "+ dbEntity.title() +" SET "+updateStr+" WHERE " +entityId+"= %s"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idValue,))
        results = cursor.fetchall()
        
        # Render success page         
        return render_template("createUpdate.j2", dbEntity=dbEntity, data=dict(request.form.items()), operation="update",updateRecord=None, formPrefillData=formPrefillData, updated=True)


@app.route('/employees/update',methods=["GET", "POST"])
def employeesUpdate():
    db_connection = db.connect_to_database()

    dbEntity = "employees"

    return update(dbEntity)
 

@app.route('/customers/update',methods=["GET", "POST"])
def customersUpdate():
    db_connection = db.connect_to_database()

    dbEntity = "customers"

    return update(dbEntity)
    


@app.route('/purchases/update',methods=["GET", "POST"])
def purchasesUpdate():
    db_connection = db.connect_to_database()

    # Declare the dbEntity
    dbEntity = "purchases"

    # Obtain data to pre-fill form fields 
    formPrefillData = {'eeIds':[],'customerIds':[]}
    # Get eeId values 
    query = "SELECT eeId FROM Employees;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    formPrefillData['eeIds'] = cursor.fetchall()
    # Get customerId values 
    query = "SELECT customerId FROM Customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    formPrefillData['customerIds'] = cursor.fetchall()
    # # Get itemId values 
    # query = "SELECT itemId FROM Items;"
    # cursor = db.execute_query(db_connection=db_connection, query=query)
    # formPrefillData['itemIds'] = [i['itemId'] for i in cursor.fetchall()] #list > template > js array
    # NEW 220306
    # Get itemId, inventoryOnHand values 
    query = "SELECT itemId, inventoryOnHand FROM Items;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    # {{formPrefillData['inventoryItems']}} to access a dict of key:val pairs: {itemIds:inventoryOnHand}
    # pass those through when the template calls addItems.js
    formPrefillData['inventoryItems'] = { str(i['itemId']):int(i['inventoryOnHand']) for i in cursor.fetchall()} #list > template > js array

    return update(dbEntity, formPrefillData=formPrefillData)


@app.route('/items/update',methods=["GET", "POST"])
def itemsUpdate():
    db_connection = db.connect_to_database()

    dbEntity = "items"

    return update(dbEntity)


# ------------------------------DELETE------------------------------

def delete(dbEntity,data):
    db_connection = db.connect_to_database()
 
    if request.method == "GET":
        deleteRecord = [i for i in request.args.items()]
        # Parse incoming request to get id attribute name (e.g., 'eeId', 'purchaseId') and its value

        entityId = deleteRecord[0][0]
        idValue = deleteRecord[0][1]
        query= "SELECT * FROM " + dbEntity.title() + " WHERE " + entityId+ " = %s" 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(idValue, ))       
        deleteRecord = (cursor.fetchall())
        

        # Render the template, pre-populated with subject's existing information from db
        return render_template("delete.j2", dbEntity=dbEntity, data=data, operation="delete", deleteRecord=deleteRecord, deleted=False)
  
    # Submit new information to confirm delete 

    if request.method == "POST":
        
        return render_template("delete.j2", dbEntity=dbEntity, data=data, operation="delete",deleteRecord=data, deleted = True) 





@app.route('/purchases/delete',methods=["GET", "POST"])
def purchasesDelete():
    db_connection = db.connect_to_database()

    dbEntity = "purchases"

    if request.method == "GET":
        purchaseId = request.args['purchaseId']

        query = "SELECT * FROM Purchases WHERE purchaseId = %s " 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(purchaseId, ))       
        data = (cursor.fetchall())

        

        return delete(dbEntity, data)

    if request.method == "POST":
        purchaseId= request.form['confirmDelete']
        #to populate
        query = "SELECT * FROM Purchases WHERE purchaseId = %s " 
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(purchaseId, ))       
        data = cursor.fetchall()

        #get all purchaseItems with given purchaseID
        query = "SELECT * FROM PurchaseItems WHERE purchaseId = %s"
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(purchaseId, ))       
        purchaseItems = (cursor.fetchall())

        
        #for all things in purchase
        for x in range(len(purchaseItems)):
            paramList = []
            itemId = str((purchaseItems[x]['itemId']))
            itemQuantity = ((purchaseItems[x]['itemQuantity']))
            

            #Place cancelled order items back in inventory 
            updateInventoryQuery = "UPDATE Items SET inventoryOnHand = inventoryOnHand + %s WHERE itemId =%s;"
            print(updateInventoryQuery)
            cursor = db.execute_query(db_connection=db_connection, query=updateInventoryQuery, query_params=(itemQuantity, itemId  ))       

            #delete PurchaseItems 
            deletePurchaseItemsquery = "DELETE FROM PurchaseItems where purchaseId =%s;"
            cursor = db.execute_query(db_connection=db_connection, query=deletePurchaseItemsquery, query_params=(purchaseId, ))       


        deletePurchases = "DELETE FROM Purchases WHERE purchaseId = %s;"
        print(deletePurchases)
        cursor = db.execute_query(db_connection=db_connection, query=deletePurchases, query_params=(purchaseId, ))    



        return delete(dbEntity, data)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3838))
    app.run(host='localhost.',port=port, debug=True)

# ------------------------------ERROR HANDLER------------------------------

#https://www.geeksforgeeks.org/python-404-error-handling-in-flask/
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    e = str(e)
# defining function
    return render_template("error/error.j2",errorType=e[:e.find(":")],errorMessage=e[e.find(":")+1:])