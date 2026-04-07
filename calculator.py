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

def is_valid_input_and_calculate(inputs: Union[Tuple[Union[int, float], ...]]) -> float:
    check_inputs(*inputs)
    return sum(inputs)

def main():
    try:
        print(is_valid_input_and_calculate((1, 2, 3)))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

def calculate_with_logging(*args: Union[Tuple[Union[int, float], ...]]) -> float:
    try:
        result = sum(args)
        print(f"Result: {result}")
        return result
    except TypeError as e:
        print(f"Warning: {e}")
        return None

def validate_and_calculate_with_logging(*args: Union[Tuple[Union[int, float], ...]]) -> float:
    if not check_inputs(*args):
        raise ValueError("Invalid input")
    return calculate_with_logging(*args)

def add_or_calculate_with_logging(op: callable, *args: Union[Tuple[Union[int, float], ...]]) -> float:
    try:
        result = op(*args)
        print(f"Result: {result}")
        return result
    except TypeError as e:
        print(f"Warning: {e}")
        return None

def wrap_and_log_result(op: callable, *args: Union[Tuple[Union[int, float], ...]]) -> float:
    try:
        result = op(*args)
        print(f"Result: {result}")
        return result
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main2():
    wrap_and_log_result(add, 1, 2)

if __name__ == "__main__":
    main2()

def log_input(*inputs: Union[Tuple[Union[int, float], ...]]) -> None:
    print(f"Inputs: {', '.join(map(str, inputs))}")

def wrapped_main2():
    log_input(1, 2)
    wrap_and_log_result(add, 1, 2)

if __name__ == "__main__":
    wrapped_main2()