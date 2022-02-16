CREATE TABLE `Customers` (
  `customerId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `customerFirstName` varchar(35) NOT NULL,
  `customerLastName` varchar(35) NOT NULL,
  `customerEmail` varchar(254),
 `membershipStatus` tinyint(1) NOT NULL,
  PRIMARY KEY (`customerID`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

CREATE TABLE `Items` (
  `itemId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `itemName` varchar(35) NOT NULL,
  `itemPrice` decimal(2) NOT NULL,
  `itemDescription` varchar(254),
  `inventoryOnHand` varchar(15) NOT NULL,
  PRIMARY KEY (`itemId`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

CREATE TABLE `Employees` (
  `eeId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `eeFirstName` varchar(35) NOT NULL,
  `eeLastName` varchar(35) NOT NULL,
  `eeEmail` varchar(254),
  `eeBday` date, 
  `position` varchar(35) NOT NULL,
  PRIMARY KEY (`eeId`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

CREATE TABLE `Purchases` (
  `purchaseId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `customerId` int(11) NOT NULL,
  `purchaseDate`date NOT NULL,
  `creditCardNumb` varchar(19) NOT NULL,
  `creditCardExp` varchar(4),
  `costOfSale` decimal(2),
  `eeId` int(11),
  FOREIGN KEY (`customerId`)
  REFERENCES Customers (`customerId`),
  FOREIGN KEY (`eeId`)
  REFERENCES Employees (`eeId`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;


CREATE TABLE `PurchaseItems` (
  `purchaseId` int(11) NOT NULL,
  `itemId` int(11) NOT NULL,
  `itemQuantity` int(3) NOT NULL,
  FOREIGN KEY (`purchaseId`)
  REFERENCES Purchases (`purchaseId`),
  FOREIGN KEY (`itemId`)
  REFERENCES Items (`itemId`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;