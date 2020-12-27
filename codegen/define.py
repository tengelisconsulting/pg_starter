from typez import FnArg, FnRecord


def _get_args_sql(fn: FnRecord) -> str:
    """
    Now, apply to all args.
    In the future, have multiple bodies for default args.
    """
    return ",\n      ".join([
        f"{fn.args[i].name} => ${fn.args[i].name}::{fn.args[i].type}"
        for i in range(len(fn.args))
    ])


def get_calling_sql(schema: str, fn: FnRecord) -> str:
    arg_sql = _get_args_sql(fn)
    return f"""\"\"\"
    SELECT {schema}.{fn.name}(
      {arg_sql}
    )
    \"\"\""""

def type_lookup(typename: str) -> str:
    return {
        "text": "String",
        "integer": "Int",
        "uuid": "String",
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
    ret_type = type_lookup(fn.ret_type)
    impl = f"""  def {fn.name}({impl_fn_args}) = sql{calling_sql}.as[{ret_type}]\n"""
    return impl


def get_impl_language_wrapping_def(contents: str) -> str:
    return f"""import slick.jdbc.PostgresProfile.api._

object DDB {{

{contents}
}}
"""
