def sum(a: int | float, b: int | float) -> int | float:
    """
    >>> sum(7,5)
    12
    >>> sum(4, -2)
    2
    """
    return a + b

def subtrac(a: int | float, b: int | float) -> int | float:
    return a - b

def multiply(a: int | float, b: int | float) -> int | float:
    return a * b

def divide(a: int | float, b: int | float) -> int | float:
    """
    >>> divide(2, 0)
    Traceback (most recent call last):
    ...
    ValueError: Zero division error
    """
    if 0 in [a, b]:
        raise ValueError("Zero division error")
    return a / b