from typing import Union, Tuple

def add(a: Union[int, float], b: Union[int, float]) -> float:
    if isinstance(b, (int, float)):
        return a + b
    raise ValueError("Second operand must be an integer or a float")

def add_with_logging(*args: Union[Tuple[Union[int, float], ...]]) -> float:
    try:
        result = sum(args)
        print(f"Result: {result}")
        return result
    except TypeError as e:
        print(f"Warning: {e}")
        return None

def check_inputs(*inputs: Union[Tuple[Union[int, float], ...]]) -> bool:
    for arg in inputs:
        if not isinstance(arg, (int, float)):
            raise ValueError("All operands must be integers or floats")

def is_valid_input(*inputs: Union[Tuple[Union[int, float], ...]]) -> None:
    check_inputs(*inputs)
    return