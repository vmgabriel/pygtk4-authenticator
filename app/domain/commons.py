import dataclasses


@dataclasses.dataclass
class Error:
    code: int
    message: str
    description: str
