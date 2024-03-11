******************************************************************************************************************************************************
In This:
1. https://www.apachefriends.org/download.html (XAMPP)
2. https://www.heidisql.com/download.php (heidisql)
3. https://www.jetbrains.com/pycharm/ (Pycham)
******************************************************************************************************************************************************
And Used Python Modules are:
1. tkinter
2. mysql.connector
3. random
******************************************************************************************************************************************************
CREATE TABLE `atm_interface` (
	`USERID` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`Name` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`Email` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`DOB` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`Pin` INT(6) NULL DEFAULT NULL,
	`Money` INT(50) NULL DEFAULT NULL
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;
******************************************************************************************************************************************************
