CREATE TABLE `Customers` (
  `customerId` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `customerFirstName` varchar(35) NOT NULL,
  `customerLastName` varchar(35) NOT NULL,
  `customerEmail` varchar(254),
 `membershipStatus` tinyint(1) NOT NULL,
  PRIMARY KEY (`customerID`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
