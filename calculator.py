def process_and_call_wrapper(func: callable) -> Union[callable, None]:
    def wrapper(*args):
        if len(args) != len(processed_args):  # Added check
            raise ValueError(f"Incorrect number of arguments for {func.__name__}")
        return func(*args) if callable(func) else None
    return wrapper if callable(func) and func is not None else None