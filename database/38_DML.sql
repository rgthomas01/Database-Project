/* 38 Cycles DML File */
/*  '%s' are were data will be input by the user    */

/****************************************************
Customers
****************************************************/

/*Retrieve All*/
Select * FROM Customers;

/*Search by ID, FirstName, LastName, or Email  */
/*likely if statement structure for selects and default passed values if fields are blank
If ID = Null replace with " " else id == id*  --based on stack post,
*/
SELECT customerId, customerFirstName, customerLastName, customerEmail, membershipStatus from Customers Where customerId = '%s' OR customerFirstName='%s' OR customerLastName='%s' OR customerEmail='%s';

/*Insert*/
/*if blank pass Null*/
INSERT INTO Customers (customerId, customerFirstName, customerLastName, customerEmail, membershipStatus)
Values (NULL, '%s','%s','%s','%s');


/*Update*/  
/*grab item passed to update by id */
UPDATE Customers SET customerFirstName = '%s', customerLastName = '%s', customerEmail = '%s', membershipStatus = '%s' WHERE customerId ='%s';

/*Delete*/
DELETE FROM Customers WHERE customerId = '%';


/****************************************************
Employees
****************************************************/
/*Retrieve All*/
Select * FROM Employees;

/*Search by ID, FirstName, LastName, */
/*likely if statement structure for selects and default passed values if fields are blank
If ID = Null replace with " " else id == id*  --based on stack post,
*/
SELECT eeId, eeFirstName, eeLastName from Employees Where eeId = '%s' OR eeFirstName='%s' OR eeLastName='%s';

/*Insert*/
/*if blank value Null*/
INSERT INTO Employees (eeId, eeFirstName, eeLastName,eePosition)
Values (NULL, '%s','%s','%s');


/*Update*/  
/*grab item passed to update by id */
SELECT * FROM Employees WHERE eeId = '%s';
UPDATE Employees SET eeFirstName = '%s', eeLastName = '%s', eePosition = '%s' WHERE eeId ='%s';

/*Delete*/
DELETE FROM Employees WHERE eeId = '%';

/****************************************************
Items
****************************************************/

/*Retrieve All*/
Select * FROM Items;

/*Search by ID, itemName, itemPrice, or itemType  */
/*likely if statement structure for selects and default passed values if fields are blank
If ID = Null replace with " " else id == id*  --based on stack post,
*/
SELECT itemId, itemName, itemPrice, itemType from Items Where itemId = '%s' OR itemName='%s' OR itemPrice='%s' OR itemType='%s';

/*Insert*/
/*if blank pass Null*/
INSERT INTO Items (itemId, itemName, itemPrice, itemDescription, itemType, inventoryOnHand)
Values (NULL,'%s','%s','%s','%s','%s');


/*Update*/  
/*grab item passed to update by id */
SELECT * FROM Items WHERE itemId = '%s';
UPDATE Items SET itemId = '%s', itemName = '%s', itemPrice = '%s', itemDescription = '%s',itemType = '%s', inventoryOnHand='%' WHERE itemId ='%s';

/*Delete*/
DELETE FROM Items WHERE itemId = '%';

/****************************************************
Purchases
***************************************************/
/*Retrieve All*/
Select * FROM Purchases;   /*depending on how we choose to display will need a join with Purchase items

*Search by purchaseID, customerId, purchaseDate, or eeID  */
/*likely if statement structure for selects and default passed values if fields are blank
If ID = Null replace with " " else id == id*  --based on stack post,
*/
SELECT purchaseId, customerId, purchaseDate, creditCardNumb, creditCardExp, costOfSale, eeId from Purchases Where purchaseId = '%s' OR customerId='%s' OR purchaseDate='%s' OR eeId='%s';
    /*depending how we decide to display will need a join with Purchase Items*/
    

/*Insert*/
/*if blank pass Null*/
INSERT INTO Purchases (purchaseId, customerId, purchaseDate, creditCardNumb, creditCardExp, costOfSale, eeId)
Values (NULL, '%s', 28,'%s','%s','%s','%s');

INSERT INTO PurchaseItems (purchaseId, itemId, itemQuantity)
Values ('%s','%s','%s');

/*Delete*/
DELETE FROM Purchases WHERE purchaseId = '%';