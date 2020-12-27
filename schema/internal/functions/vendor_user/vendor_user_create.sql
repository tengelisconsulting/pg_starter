CREATE OR REPLACE FUNCTION vendor_user_create(
  IN p_vendor_id  UUID,
  IN p_user_id  UUID,
  IN p_relationship  INTEGER
)
RETURNS INTEGER
AS $$
BEGIN
  INSERT INTO vendor_user (
                vendor_id,
                user_id,
                relationship
              )
       VALUES (
                p_vendor_id,
                p_user_id,
                p_relationship
              )
  ;
  RETURN 1;
END;
$$
LANGUAGE plpgsql
;
