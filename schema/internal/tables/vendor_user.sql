CREATE TABLE IF NOT EXISTS vendor_user (
  vendor_id  UUID   NOT NULL
    REFERENCES vendor (vendor_id)  ON DELETE CASCADE,
  user_id  UUID   NOT NULL
    REFERENCES ac_user (user_id)  ON DELETE CASCADE,

  relationship  INTEGER  NOT NULL,

  PRIMARY KEY (vendor_id, user_id)
);

COMMENT ON COLUMN vendor_user.relationship IS '0: creator, 1: member';
