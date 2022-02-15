CREATE TABLE `Customers` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `customer_first_name` varchar(35) NOT NULL,
  `customer_last_name` varchar(35) NOT NULL,
  `customer_email` varchar(254),
 `membership_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
