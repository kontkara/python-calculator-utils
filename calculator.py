def check_result(func: callable, *args: Union[Tuple[Union[int, float], ...]]) -> None:
    try:
        result = func(*args)
        if isinstance(result, (int, float)):
            print(f"Result: {result}")
        else:
            print("Non-numeric result")
    except Exception as e:
        print(f"Error: {e}")