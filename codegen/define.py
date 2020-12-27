from typez import FnArg, FnRecord


def _get_args_sql(fn: FnRecord) -> str:
    """
    Now, apply to all args.
    In the future, have multiple bodies for default args.
    """
    return ",\n      ".join([
        f"{fn.args[i].name} => ?::{fn.args[i].type}"
        for i in range(len(f.args))
    ])


def get_calling_sql(schema: str, fn: FnRecord) -> str:
    arg_sql = _get_args_sql(fn)
    return f"""
    SELECT {schema}.{fn.name}(
      {arg_sql}
    )
    """

def type_lookup(typename: str) -> str:
    return {
        "text": "String",
        "integer": "Int",
    }[typename]


def get_impl_language_args(fn: FnRecord) -> str:
    def fmt_arg(arg: FnArg) -> str:
        arg_type = type_lookup(arg.type)
        return f"{arg.name}: {arg_type}"
    arg_s = ", ".join([fmt_arg(arg) for arg in fn.args])
    return arg_s


def get_impl_language_def(schema: str, fn: FnRecord) -> str:
    calling_sql = get_calling_sql(schema, fn)
    impl_fn_args = get_impl_language_args(fn)
    impl_query_args = ", ".join([a.name for a in fn.args])
    impl = f"""
def {fn.name}(con: Connection, {impl_fn_args}) = {{
  val statement = con.createStatement()
  val resultSet = statement.executeQuery({calling_sql}
    , [{impl_query_args}]
  )
  resultSet
}}"""
    return impl
