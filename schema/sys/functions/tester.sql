CREATE OR REPLACE FUNCTION sys.tester(
  IN p_thing  TEXT,
  IN p_thing_2  TEXT,
  IN p_thing_3  TEXT = 'hello'
)
RETURNS INTEGER
AS $$
BEGIN
  RETURN 2;
END;
$$
LANGUAGE plpgsql
;
