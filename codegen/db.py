import os
from typing import List, NamedTuple, Tuple, Optional, Any

import psycopg2

from typez import FnArg, FnRecord


RawFn = Tuple[str, str]


con = None


def _to_fn_arg(arg_row: List[str])-> FnArg:
    if len(arg_row) == 2:
        # [<var_name>, <var_type>]
        return FnArg(name=arg_row[0], type=arg_row[1])
    # [<var_name>, <var_type>, DEFAULT, <default_val::type>]
    assert 'DEFAULT' == arg_row[2]
    default = arg_row[3].split("::")[0]
    return FnArg(
        name=arg_row[0],
        type=arg_row[1],
        default=default
    )


def _parse_raw_fn(raw: RawFn) -> FnRecord:
    name = raw[0]
    ret_type = raw[1]
    args = [a.split(" ") for a in raw[2].split(", ")]
    fn_args = [_to_fn_arg(a) for a in args]
    return FnRecord(
        name=name,
        ret_type=ret_type,
        args=fn_args,
    )


def _fetch_schema_functions(
        cur, schema
) -> List[RawFn]:
    sql = """
      SELECT p.proname fn_name,
             pg_get_function_result(p.oid),
             pg_get_function_arguments(p.oid) args
        FROM pg_proc p
        JOIN pg_namespace ns
          ON (p.pronamespace = ns.oid)
       WHERE ns.nspname = %s;
    """
    cur.execute(sql, [schema])
    return cur.fetchall()


def _with_cur(fn):
    def impl(*args, **kwargs):
        cur = con.cursor()
        try:
            res = fn(cur, *args, **kwargs)
        finally:
            cur.close()
        return res
    return impl


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


def load_schema_functions(schema) -> List[FnRecord]:
    raw_fns = _with_cur(_fetch_schema_functions)(schema)
    return [_parse_raw_fn(f) for f in raw_fns]
