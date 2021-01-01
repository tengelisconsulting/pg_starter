"""
# this expects the json(b) decoder to be as such:
await conn.set_type_codec(
            'json',
            encoder=json.dumps,
            decoder=json.loads,
            schema='pg_catalog'
        )
"""
from typez import DefineLang, FnArg, FnRecord


def _get_calling_sql(schema: str, fn: FnRecord) -> str:
    arg_sql = ",\n      ".join([
        f"{fn.args[i].name} => ${i + 1}::{fn.args[i].type}"
        for i in range(len(fn.args))
    ])
    bindargs = ", ".join([arg.name for arg in fn.args])
    return f"""return await con.fetchval(\"\"\"
    SELECT {schema}.{fn.name}(
      {arg_sql}
    )
    \"\"\", {bindargs})"""


def _type_lookup(typename: str) -> str:
    return {
        "text": "str",
        "integer": "int",
        "uuid": "str",
        "json": "Dict",
        "jsonb": "Dict",
    }[typename]


def _get_fn_args(fn: FnRecord) -> str:
    def fmt_arg(arg: FnArg) -> str:
        arg_type = _type_lookup(arg.type)
        if arg.default is None:
            return f"{arg.name}: {arg_type}"
        new_default = arg.default
        if arg.default == "NULL":
            new_default = "None"
        return f"{arg.name}: {arg_type} = {new_default}"
    return ", ".join([fmt_arg(arg) for arg in fn.args])


def get_impl_language_fn_def(schema: str, fn: FnRecord) -> str:
    calling_sql = _get_calling_sql(schema, fn)
    impl_fn_args = _get_fn_args(fn)
    ret_type = _type_lookup(fn.ret_type)
    impl = f"""def {fn.name}(con, {impl_fn_args}) -> {ret_type}:
    {calling_sql}

"""
    return impl


def wrap_function_defs(contents: str) -> str:
    return contents
