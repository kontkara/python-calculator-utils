python
def check_result(func: callable, *args: Union[Tuple[Union[int, float], ...], None]) -> None:
    try:
        result = func(*args)
        if isinstance(result, (int, float)):
            print(f"Result: {result}")
        elif result is not None:
            print("Non-numeric result")
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if isinstance(result, (int, float)):
            return result