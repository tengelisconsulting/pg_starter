CREATE OR REPLACE FUNCTION sys.tester(
  IN p_thing  TEXT,
  IN p_thing_2  TEXT
)
RETURNS TEXT
AS $$
BEGIN
  RETURN p_thing;
END;
$$
LANGUAGE plpgsql
;
