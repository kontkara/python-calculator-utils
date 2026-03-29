from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> float:
    if isinstance(b, (int, float)):
        return a + b
    raise ValueError("Second operand must be an integer or a float")

def add_with_logging(*args: Union[int, float]) -> float:
    """Log warning for non-numeric inputs"""
    try:
        return sum(args)
    except TypeError as e:
        print(f"Warning: {e}")
        return None