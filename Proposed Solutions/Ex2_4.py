# mutint.py


class MutInt:
    __slots__ = ["value"]

    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"MutInt({self.value!r})"

    def __format__(self, format_spec: str) -> str:
        return format(self.value, format_spec)

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    __radd__ = __add__
