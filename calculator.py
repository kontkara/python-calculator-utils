from typing import Union, Tuple, Optional

def check_result(func: callable, *args: Union[Tuple[Union[int, float], ...], None]) -> Optional[float]:
    try:
        result = func(*args)
        if isinstance(result, (int, float)):
            print(f"Result: {result}")
            return result  # Return the result
        elif result is not None:
            print("Non-numeric result")
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if result is not None and not isinstance(result, (int, float)):
            raise ValueError(f"Unexpected non-numeric result: {result}")

def get_result(func: callable, *args: Union[Tuple[Union[int, float], ...], None]) -> Optional[float]:
    try:
        result = check_result(func, *args)
        if isinstance(result, (int, float)):
            return result
        else:
            raise ValueError(f"get_result should not return {result}")
    except ValueError as e:
        raise ValueError(f"Unexpected non-numeric result: {e}") from None

def _process_args(*args: Union[Tuple[Union[int, float], ...], None]) -> Tuple[Optional[float]]:
    return tuple(arg if isinstance(arg, (int, float)) else None for arg in args)

def process_and_call(func: callable, *args: Union[Tuple[Union[int, float], ...], None]) -> Optional[float]:
    processed_args = _process_args(*args)
    try:
        result = check_result(func, *processed_args)
        return result
    except ValueError as e:
        raise ValueError(f"Invalid input for {func.__name__}: {e}") from None

def process_and_call_wrapper(func: callable) -> Union[callable, None]:
    def wrapper(*args):
        return process_and_call(func, *args)
    return wrapper if func else None