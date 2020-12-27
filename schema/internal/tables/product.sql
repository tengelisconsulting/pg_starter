CREATE TABLE IF NOT EXISTS product (
  product_id  UUID   NOT NULL  DEFAULT uuid_generate_v1mc(),
  created  TIMESTAMPTZ  NOT NULL  DEFAULT now(),
  updated  TIMESTAMPTZ  NOT NULL  DEFAULT now(),

  product_code  TEXT  NOT NULL
    UNIQUE,
  status  INTEGER  NOT NULL,

  qr_code  BYTEA  DEFAULT NULL,
  images  TEXT[]  DEFAULT ARRAY[]::TEXT[],
  physical_info JSONB  DEFAULT NULL,
  price_info  JSONB  DEFAULT NULL,

  adhoc  JSONB  DEFAULT NULL,

  PRIMARY KEY (product_id)
);

COMMENT ON COLUMN product.status IS '0: active, 1: archived, 2: disabled';
