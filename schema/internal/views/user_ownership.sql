CREATE OR REPLACE VIEW user_ownership
AS
  --  vendors
     SELECT u.user_id,
            vu.vendor_id obj_id
       FROM ac_user u
       JOIN vendor_user vu
         ON vu.user_id = u.user_id
      WHERE vu.relationship IN (0, 1)
  --  products
  UNION ALL
     SELECT u.user_id,
            vp.product_id obj_id
       FROM ac_user u
       JOIN vendor_user vu
         ON vu.user_id = u.user_id
       JOIN vendor_product vp
         ON vp.vendor_id = vu.vendor_id

;
