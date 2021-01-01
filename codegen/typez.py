from enum import Enum
from typing import List, NamedTuple, Tuple, Optional, Any, Union, Literal


class DefineLang(Enum):
    scala = "scala"
    python = "python"


class FnArg(NamedTuple):
    name: str
    type: str
    default: Optional[Any] = None


class FnRecord(NamedTuple):
    name: str
    ret_type: str
    args: List[FnArg]
