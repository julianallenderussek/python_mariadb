CREATE DEFINER=`root`@`localhost` PROCEDURE `python_procedures`.`get_items`()
--     MODIFIES SQL DATA
begin
	SELECT * FROM items;
END