CREATE OR REPLACE FUNCTION vendor_create(
  IN p_vendor_name  TEXT,
  IN p_adhoc  JSONB  DEFAULT NULL
)
RETURNS UUID
AS $$
DECLARE
  v_vendor_id  UUID  := new_uuid();
BEGIN
  INSERT INTO vendor (
                vendor_id,
                vendor_name,
                adhoc
              )
       VALUES (
                v_vendor_id,
                p_vendor_name,
                p_adhoc
              )
  ;
  RETURN v_vendor_id;
END;
$$
LANGUAGE plpgsql
;
