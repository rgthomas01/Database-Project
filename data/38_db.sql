CREATE TABLE `Customers` (
  `customerId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `customerFirstName` varchar(35) NOT NULL,
  `customerLastName` varchar(35) NOT NULL,
  `customerEmail` varchar(254),
 `membershipStatus` tinyint(1) NOT NULL,
  PRIMARY KEY (`customerID`)
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

