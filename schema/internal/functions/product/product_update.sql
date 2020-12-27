CREATE OR REPLACE FUNCTION product_update(
  IN p_product_id  UUID,
  IN p_status  INTEGER  DEFAULT NULL,
  IN p_qr_code  BYTEA  DEFAULT NULL,
  IN p_images  TEXT[]  DEFAULT NULL,
  IN p_physucal_info JSONB  DEFAULT NULL,
  IN p_price_info  JSONB  DEFAULT NULL,
  IN p_adhoc  JSON  DEFAULT NULL
)
RETURNS INTEGER
AS $$
DECLARE
  v_updated  INTEGER  := 0;
BEGIN
  IF (SELECT 1
        FROM product
       WHERE product_id = p_product_id) IS NULL THEN
    RETURN 0;
  END IF;

  IF p_status IS NOT NULL THEN
    UPDATE product
       SET status = p_status
     WHERE product_id = p_product_id
    ;
    v_updated := 1;
  END IF;

  IF p_qr_code IS NOT NULL THEN
    UPDATE product
       SET qr_code = p_qr_code
     WHERE product_id = p_product_id
    ;
    v_updated := 1;
  END IF;

  IF p_images IS NOT NULL THEN
    UPDATE product
       SET images = p_images
     WHERE product_id = p_product_id
    ;
    v_updated := 1;
  END IF;

  IF p_physical_info IS NOT NULL THEN
    UPDATE product
       SET physical_info = p_physical_info
     WHERE product_id = p_product_id
    ;
    v_updated := 1;
  END IF;

  IF p_price_info IS NOT NULL THEN
    UPDATE product
       SET price_info = p_price_info
     WHERE product_id = p_product_id
    ;
    v_updated := 1;
  END IF;

  IF p_adhoc IS NOT NULL THEN
    UPDATE product
       SET adhoc = p_adhoc
     WHERE product_id = p_product_id
    ;
    v_updated := 1;
  END IF;

  IF v_updated = 1 THEN
    UPDATE product
       SET updated = now()
     WHERE product_id = p_product_id
    ;
  END IF;

  RETURN v_updated;
END;
$$
LANGUAGE plpgsql
;
