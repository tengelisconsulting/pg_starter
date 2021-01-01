from typing import List

from typez import DefineLang, FnRecord
from . import scala_define


def _get_def_module(lang: DefineLang):
    return {
        DefineLang.scala: scala_define,
        # DefineLang.python: scala_define,
    }[lang]


def get_def_file_contents(schema: str, lang: DefineLang, fns: List[FnRecord]) -> str:
    def_module = _get_def_module(lang)
    impl_language_defs = [
        def_module.get_impl_language_fn_def(schema, fn) for fn in fns]
    fn_defs = "\n".join(impl_language_defs)
    return def_module.wrap_function_defs(fn_defs)
