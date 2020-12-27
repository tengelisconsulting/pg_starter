CREATE OR REPLACE FUNCTION product_order_create(
  IN p_quantity  INTEGER,
  IN p_product_id  UUID,
  IN p_pickup_time  TIMESTAMPTZ,
  IN p_user_info  JSONB,
  IN p_adhoc  JSONB  DEFAULT NULL
)
RETURNS UUID
AS $$
DECLARE
  v_order_id  UUID  := new_uuid();
BEGIN
  INSERT INTO product_order (
                order_id,
                product_id,
                quantity,
                pickup_time,
                user_info,
                adhoc
              )
       VALUES (
                v_order_id,
                p_product_id,
                p_quantity,
                p_pickup_time,
                p_user_info,
                p_adhoc
              )
  ;
  RETURN v_order_id;
END;
$$
LANGUAGE plpgsql
;
