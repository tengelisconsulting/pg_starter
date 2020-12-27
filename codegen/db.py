import os

import psycopg2


# con = None


def with_cur(fn):
    def impl(*args, **kwargs):
        cur = con.cursor()
        try:
            res = fn(cur, *args, **kwargs)
        finally:
            print("closing...")
            cur.close()
        return res
    return impl


def _fetch_schema_functions(cur, schema):
    sql = """
      SELECT p.proname fn_name,
             pg_get_function_arguments(p.oid) args
        FROM pg_proc p
        JOIN pg_namespace ns
          ON (p.pronamespace = ns.oid)
       WHERE ns.nspname = %s;
    """
    cur.execute(sql, [schema])
    return cur.fetchall()
fetch_schema_functions = with_cur(
    _fetch_schema_functions)


def connect(
        host=os.getenv("PGHOST", "127.0.0.1"),
        user=os.getenv("PGUSER", "postgres"),
        dbname=os.getenv("PGDB", "postgres"),
        password=os.getenv("PGPASSWORD", ""),
        port=int(os.getenv("PGPORT", "5432")),
) -> None:
    global con
    con = psycopg2.connect(
        host=host,
        user=user,
        dbname=dbname,
        password=password,
        port=port,
    )
    return


def shutdown():
    con.close()
