CREATE TABLE IF NOT EXISTS vendor (
  vendor_id  UUID   NOT NULL  DEFAULT uuid_generate_v1mc(),
  created  TIMESTAMPTZ  NOT NULL  DEFAULT now(),
  updated  TIMESTAMPTZ  NOT NULL  DEFAULT now(),

  vendor_name  TEXT  NOT NULL
    UNIQUE,

  adhoc  JSONB  DEFAULT NULL,

  PRIMARY KEY (vendor_id)
);
