from typing import List, NamedTuple, Tuple, Optional, Any, Union


DefineMode = Union[
    "scala"
]


class FnArg(NamedTuple):
    name: str
    type: str
    default: Optional[Any] = None


class FnRecord(NamedTuple):
    name: str
    ret_type: str
    args: List[FnArg]
