from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> float:
    if isinstance(b, (int, float)):
        return a + b
    raise ValueError("Second operand must be an integer or a float")