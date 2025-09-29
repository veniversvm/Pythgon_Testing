def sum(a: int | float, b: int | float) -> int | float:
    return a + b

def subtrac(a: int | float, b: int | float) -> int | float:
    return a - b

def multiply(a: int | float, b: int | float) -> int | float:
    return a * b

def divide(a: int | float, b: int | float) -> int | float:
    if 0 in [a, b]:
        raise ValueError("Zero division error")
    return a / b