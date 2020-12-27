import os
from typing import List, NamedTuple, Tuple

import psycopg2


RawFn = Tuple[str, str]

class FnArg(NamedTuple):
    name: str
    type: str


class FnRecord(NamedTuple):
    name: str
    args: List[FnArg]


# con = None


def _parse_raw_fn(raw: RawFn) -> FnRecord:
    name = raw[0]
    args = [a.split(" ") for a in raw[1].split(", ")]
    fn_args = [FnArg(name=a[0], type=a[1]) for a in args]
    return FnRecord(name=name, args=fn_args)


def _fetch_schema_functions(
        cur, schema
) -> List[RawFn]:
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
    return


def with_cur(fn):
    def impl(*args, **kwargs):
        cur = con.cursor()
        try:
            res = fn(cur, *args, **kwargs)
        finally:
            cur.close()
        return res
    return impl


fetch_schema_functions = with_cur(_fetch_schema_functions)
