CREATE TABLE IF NOT EXISTS product_order (
  order_id  UUID   NOT NULL  DEFAULT uuid_generate_v1mc(),
  created  TIMESTAMPTZ  NOT NULL  DEFAULT now(),
  updated  TIMESTAMPTZ  NOT NULL  DEFAULT now(),

  product_id  UUID   NOT NULL
    REFERENCES product (product_id)  ON DELETE CASCADE,
  quantity  INTEGER  NOT NULL,
  pickup_time  TIMESTAMPTZ  NOT NULL,
  user_info  JSONB,

  adhoc  JSONB  DEFAULT NULL,

  PRIMARY KEY (order_id)
);
