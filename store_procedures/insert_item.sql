CREATE DEFINER=`root`@`localhost` PROCEDURE `python_procedures`.`insert_item`(name VARCHAR(100), price FLOAT)
    MODIFIES SQL DATA
begin
	INSERT INTO python_procedures.items (name, price) VALUES(name, price);
END