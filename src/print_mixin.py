class PrintMixin:
    description: str
    name: str

    def __init__(self, should_print: bool = True) -> None:
        if should_print:
            print(repr(self))

    def __repr__(self) -> str:
        result: str = f"{self.__class__.__name__}({self.name}, {self.description}"
        if hasattr(self, "price"):
            result += f", {self.price}"
        if hasattr(self, "quantity"):
            result += f", {self.quantity}"
        result += ")"
        return result
