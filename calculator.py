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

def add_and_log_input(op: callable, *args: Union[Tuple[Union[int, float], ...]]) -> float:
    try:
        result = op(*args)
        log_input(args)
        print(f"Result: {result}")
        return result
    except ValueError as e:
        print(f"Error: {e}")
        return None

def wrapped_main():
    result = add_and_log_input(is_valid_input_and_calculate, (1, 2, 3))
    if result is None:
        print("Error occurred during calculation")

if __name__ == "__main__":
    wrapped_main()