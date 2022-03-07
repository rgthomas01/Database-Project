/* 38 Cycles DML File */
/*  '%s' are were data will be input by the user , there are also variable introduced
within the code such as NewQuantity that will by dynamically generated the utilized
These vairables are introduced in comments preceding their appearance in the DML   */

/****************************************************
Customers
****************************************************/

/***********READ***********/

/*Retrieve All*/
Select * FROM Customers;

/*Retrieve by param*/
/*Search by ID, FirstName, LastName, Email, or any combination of those 4   */
/*Search string is dynamically built based on which params are passed*/

SELECT customerId, customerFirstName, customerLastName, customerEmail, membershipStatus from Customers Where customerId = '%s'  AND customerFirstName='%s' AND customerLastName='%s' AND customerEmail='%s';

/***********CREATE***********/
/*if customerEmail is Null*/
INSERT INTO Customers (customerId, customerFirstName, customerLastName, customerEmail, membershipStatus)
Values (NULL, '%s','%s','%s','%s');

/*if all values are present*/
INSERT INTO Customers (customerId, customerFirstName, customerLastName, customerEmail, membershipStatus)
Values (NULL, '%s','%s','%s','%s');


/************UPDATE************/  
/*grab item passed to update by id */
SELECT * FROM Customers WHERE customerId = '%'
/*then Update */
UPDATE Customers SET customerFirstName = '%s' customerLastName = '%s' customerEmail = '%s'
 membershipStatus = '%s' WHERE customerId ='%s';



/****************************************************
Employees
****************************************************/

/***********READ***********/

/*Retrieve All*/
Select * FROM Employees;

/*Retrieve by param*/
/*Search by ID, FirstName, LastName or any combination of the 3  */
/*Search string is dynamically built based on which params are passed this example given is if all 3 are passed*/



/***********CREATE***********/
INSERT INTO Employees (eeId, eeFirstName, eeLastName,eePosition,eeStatus)
Values (NULL, '%s','%s','%s','%s');


/***********UPDATE***********/  
/*grab item passed to update by id */
SELECT * FROM Employees WHERE eeId = '%s';

/*then Update*/
UPDATE Employees SET eeFirstName = '%s', eeLastName = '%s', eePosition = '%s', eeStatus = '%s' WHERE eeId ='%s';

/***********DELETE ***********/
/*Replace eeId with Null in all Purchases ee is affiliated with */
UPDATE Purchases SET eeId = NULL WHERE eeID =%s; 
/*then delete employee from DB*/
DELETE FROM Employees WHERE eeId = '%';

/****************************************************
Items
****************************************************/

/***********READ***********/

/*Retrieve All*/
Select * FROM Items;

/*Retrieve by param*/
/*Search by ID, itemName, itemPrice, or itemType  */
/*Search string is dynamically built based on which params are passed this example given is if all 4 are passed*/
SELECT itemId, itemName, itemPrice, itemType from Items Where itemId = '%s' AND itemName='%s' AND itemPrice='%s' AND itemType='%s';

/***********CREATE***********/

INSERT INTO Items (itemId, itemName, itemPrice, itemDescription, itemType, inventoryOnHand)
Values (NULL,'%s','%s','%s','%s','%s');


/***********UPDATE***********/  
/*grab item passed to update by id */
SELECT * FROM Items WHERE itemId = '%s';
/*then update*/
UPDATE Items SET itemId = '%s' itemName = '%s' itemPrice = '%s' itemDescription = '%s' itemType = '%s' inventoryOnHand='%' WHERE itemId ='%s';



/****************************************************
Purchases & Purchase Items
***************************************************/

/***********READ***********/

/*Retrieve All*/
Select * FROM Purchases;  

/*Retrieve by param*/
/*Search by purchaseID, customerId, purchaseDate, or eeID  */
/*Search string is dynamically built based on which params are passed this example given is if all 4 are passed*/

SELECT purchaseId, customerId, purchaseDate, eeId from Purchases Where purchaseId = '%s' AND customerId='%s' AND purchaseDate='%s' AND eeId='%s';

    
/************CREATE************/
/*Create Purchase*/
/*If eeId is included in transaction*/
INSERT INTO Purchases (purchaseId, customerId, purchaseDate, creditCardNumb, creditCardExp, costOfSale, eeId) VALUES (NULL, %s,%s,%s,%s,%s,%s);

/*If eeId is none/SelfCheckout is used*/
INSERT INTO Purchases (purchaseId, customerId, purchaseDate, creditCardNumb, creditCardExp, costOfSale)
Values (NULL, '%s', '%s','%s','%s','%s');


/*Create PurchaseItems*/
/*Add items to PurchaseItems within Purchase menu*/
INSERT INTO PurchaseItems (purchaseId, itemId, itemQuantity)
Values ('28','29','%s');

/*Modify inventoryOnHand when item is added to purchase*/
/*grab quantity that needs to be modified for each item added*/
SELECT itemQuantity  FROM Items WHERE itemId = %s;
/*SET new variable, newQuantity = inventoryOnHand - itemQuantity*/
UPDATE items SET inventoryOnHand = newQuantity where itemId = %s;


/************UPDATE***********/
/*View selected Update Record*/
SELECT PurchaseItems.itemId, PurchaseItems.itemQuantity
FROM PurchaseItems
JOIN Purchases ON Purchases.purchaseId = PurchaseItems.purchaseId
WHERE Purchases.purchaseId = %s;

/*Update Selected Record*/
/*First get quantity from purchaseItems*/
SELECT itemId, itemQuantity FROM PurchaseItems WHERE purchaseId = %s;
/*this will be stored in a dict, PurchaseUpdateDict, and used to update inventoryOnHand if quantity is changed */

/*Update both Purchases & PurchaseItems*/
UPDATE Purchases SET PurchaseDate=%s customerId=%s eeId = %s creditCardNumb =%
 creditCardExp =%s costOfSale =%s;
UPDATE PurchaseItems SET itemQuantity =% WHERE purchaseId =%s and itemId =%s;

/*If an itemQuantity is set to Zero in above Update*/
DELETE FROM PurchaseItems WHERE purchaseId = '%' and itemId = %s;


/*if Update changes were made to quantities compare PurchaseUpdateDict to get QuantityAdj Variable*/
UPDATE Items SET inventoryOnHand = QuantityAdj WHERE itemId =%s;



/***********DELETE***********/
/*Deletes from PurchaseItems first to elim fk constraint issue*/
DELETE FROM PurchaseItems where purchaseId = '%';
/*Then Delete from Purchases*/
DELETE FROM Purchases WHERE purchaseId = '%';



/*********** Misc Queries***********/

/*PRE-FILL FROM QUERIES */
SELECT eeId FROM Employees;
SELECT customerId FROM Customers;
SELECT itemId FROM Items;

