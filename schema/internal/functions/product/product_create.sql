CREATE OR REPLACE FUNCTION product_create(
  IN p_product_code  TEXT,
  IN p_status  INTEGER  DEFAULT 0,
  IN p_physical_info  JSONB  DEFAULT NULL,
  IN p_price_info  JSONB  DEFAULT NULL,
  IN p_adhoc  JSONB  DEFAULT NULL
)
RETURNS UUID
AS $$
DECLARE
  v_product_id  UUID  := new_uuid();
BEGIN
  INSERT INTO product (
                product_id,
                product_code,
                status,
                physical_info,
                price_info,
                adhoc
              )
       VALUES (
                v_product_id,
                p_product_code,
                p_status,
                p_physical_info,
                p_price_info,
                p_adhoc
              )
  ;
  RETURN v_product_id;
END;
$$
LANGUAGE plpgsql
;
