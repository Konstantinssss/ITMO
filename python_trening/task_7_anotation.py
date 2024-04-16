a: int = 5
b: str = 'строка'
c: list = [1, 2]
def indent(s: str, widht: int) -> str:
    return " " * (max(0, width - len(s))) + s