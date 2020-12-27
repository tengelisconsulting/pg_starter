CREATE OR REPLACE FUNCTION vendor_product_create(
  IN p_vendor_id  UUID,
  IN p_product_id  UUID
)
RETURNS INTEGER
AS $$
BEGIN
  INSERT INTO vendor_product (
                vendor_id,
                product_id
              )
       VALUES (
                p_vendor_id,
                p_product_id
              )
  ;
  RETURN 1;
END;
$$
LANGUAGE plpgsql
;
