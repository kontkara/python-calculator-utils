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

def log_input_and_call(op: callable, *args: Union[Tuple[Union[int, float], ...]]) -> float:
    try:
        if len(args) != op.__code__.co_argcount:
            raise ValueError("Number of arguments does not match the function signature")
        result = op(*args)
        print(f"Input: {args}")
        print(f"Result: {result}")
        return result
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None

def wrapped_main():
    result = log_input_and_call(lambda x: add(*x), (1, 2, 3))
    if result is None:
        print("Error occurred during calculation")

if __name__ == "__main__":
    wrapped_main()