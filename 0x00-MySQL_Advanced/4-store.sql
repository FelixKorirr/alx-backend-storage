-- Creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER //
create TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
update items
set quantity = quantity - new.amount
where item = new.item_name;
END //
DELIMITER ;
