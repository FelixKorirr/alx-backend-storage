-- Resets the valid_email when email has been changed.
DELIMITER //
create trigger reset_email
before UPDATE on users
FOR EACH ROW
begin
if old.email != new.email then
set new.valid_email = 0;
else
set new.valid_email = new.valid_email;
end if;
end //
DELIMITER ;
