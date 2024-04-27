-- Resets the valid_email when email has been changed.
DELIMITER //
create trigger reset_email
before UPDATE on users
FOR EACH ROW
begin
if old.email != new.email then
set new.valid_email = 0;
end if;
end //
DELIMITER ;
