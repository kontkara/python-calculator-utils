def process_and_call_wrapper(func: callable) -> Union[callable, None]:
    def wrapper(*args):
        if len(args) != len(processed_args):  # Added check
            raise ValueError(f"Incorrect number of arguments for {func.__name__}")
        return process_and_call(func, *args)
    return wrapper if func else None