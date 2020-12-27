CREATE TABLE IF NOT EXISTS vendor_product (
  product_id  UUID   NOT NULL
    REFERENCES product (product_id)  ON DELETE CASCADE,
  vendor_id  UUID   NOT NULL
    REFERENCES vendor (vendor_id)  ON DELETE CASCADE,

  PRIMARY KEY (vendor_id, product_id)
);
