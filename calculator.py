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