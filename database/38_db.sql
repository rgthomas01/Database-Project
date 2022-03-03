/* 38 Cycles DB File */

DROP TABLE IF EXISTS `PurchaseItems`;
DROP TABLE IF EXISTS `Purchases`;
DROP TABLE IF EXISTS `Customers`;
DROP TABLE IF EXISTS `Employees`;
DROP TABLE IF EXISTS `Items`;

CREATE TABLE `Customers` (
  `customerId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `customerFirstName` varchar(35) NOT NULL,
  `customerLastName` varchar(35) NOT NULL,
  `customerEmail` varchar(254),
 `membershipStatus` tinyint(1) NOT NULL,
  PRIMARY KEY (`customerID`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

INSERT INTO `Customers` (`customerId`, `customerFirstName`, `customerLastName`, `customerEmail`, `membershipStatus`) 
VALUES (NULL, 'John', 'Smith ', 'johnsmith@aol.com', '1');


CREATE TABLE `Items` (
  `itemId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `itemName` varchar(35) NOT NULL,
  `itemPrice` decimal(6,2) NOT NULL,
  `itemDescription` varchar(254),
  `itemType` varchar(50),
  `inventoryOnHand` varchar(15) NOT NULL,
  PRIMARY KEY (`itemId`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

INSERT INTO `Items` (`itemId`, `itemName`, `itemPrice`, `itemDescription`, `itemType`, `inventoryOnHand`) 
VALUES (NULL, 'Full Suspension Mountain Bike', '1599.99', 'goes up mountain and down', `Mountain Bike`, '21');

INSERT INTO `Items` (`itemId`, `itemName`, `itemPrice`, `itemDescription`, `itemType`, `inventoryOnHand`) 
VALUES (NULL, 'Road Bike', '449', 'white with blue rims', `Road Bike`, '21');

INSERT INTO `Items` (`itemId`, `itemName`, `itemPrice`, `itemDescription`, `inventoryOnHand`) 
VALUES (NULL, 'Road Bike', '449', 'white with purple rims', `Road Bike`, '21');

CREATE TABLE `Employees` (
  `eeId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `eeFirstName` varchar(35) NOT NULL,
  `eeLastName` varchar(35) NOT NULL,
  `eePosition` varchar(35) NOT NULL,
  `eeStatus`  tinyint(1) NOT NULL,
  PRIMARY KEY (`eeId`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

INSERT INTO `Employees` (`eeId`, `eeFirstName`, `eeLastName`,  `eePosition`, `employmentStatus`) 
VALUES (NULL, 'Paul', 'Bunion', 'floorManager', '1');

INSERT INTO `Employees` (`eeId`, `eeFirstName`, `eeLastName`,  `eePosition`, `employmentStatus`) 
VALUES (NULL, 'Laura', 'Bunion', 'floorManager', '2');

INSERT INTO `Employees` (`eeId`, `eeFirstName`, `eeLastName`,  `eePosition`, `employmentStatus`) 
VALUES (NULL, 'John', 'Smith', 'salesClerk', '1');

INSERT INTO `Employees` (`eeId`, `eeFirstName`, `eeLastName`,  `eePosition`, `employmentStatus`) 
VALUES (NULL, 'John', 'Doe', 'salesClerk', '2');


CREATE TABLE `Purchases` (
  `purchaseId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `customerId` int(11) NOT NULL,
  `purchaseDate`date NOT NULL,
  `creditCardNumb` varchar(19) NOT NULL,
  `creditCardExp` varchar(4),
  `costOfSale` decimal(6,2),
  `eeId` int(11),
  FOREIGN KEY (`customerId`)
  REFERENCES Customers (`customerId`),
  FOREIGN KEY (`eeId`)
  REFERENCES Employees (`eeId`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

INSERT INTO `Purchases` (`purchaseId`, `customerId`, `purchaseDate`, `creditCardNumb`, `creditCardExp`, `costOfSale`, `eeId`) 
VALUES (NULL, '28', '2022-02-18', '1111111111111111', '1111', '1599.99', '28');


CREATE TABLE `PurchaseItems` (
  `purchaseId` int(11) NOT NULL,
  `itemId` int(11) NOT NULL,
  `itemQuantity` int(3) NOT NULL,
  PRIMARY KEY (`purchaseId`, `itemId`),
  CONSTRAINT `PurchaseItems_ibfk_1` FOREIGN KEY (`purchaseId`)
  REFERENCES Purchases (`purchaseId`),
  CONSTRAINT `PurchaseItems_ibfk_2`FOREIGN KEY (`itemId`)
  REFERENCES Items (`itemId`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

INSERT INTO `PurchaseItems` (`purchaseId`, `itemId`, `itemQuantity`)
 VALUES ('28', '28', '1');
