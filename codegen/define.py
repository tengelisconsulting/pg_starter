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
