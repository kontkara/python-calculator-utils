def process_and_call_wrapper(func: Callable[[*Any], *Any]) -> Union[Callable[[*Any], *Any], None]:
    ...
    if check_builtin(func):  # exclude built-in functions
        pass
    elif isinstance(func, str):
        wrapped_func = safe_eval(get_lambda_name(func))
    elif callable(func) and not check_builtin(func):  
        try:
            result = func(*processed_args)
            validate_return_type(result)
            wrapped_func = lambda *args: wrapper(*args) if len(args) == len(processed_arg_names) else None
        except TypeError as e:
            raise ValueError(f"Incorrect type of arguments for {func.__name__}") from e
    else:
        return None

    if wrapped_func is not None and callable(wrapped_func):
        def with_logging(*args, **kwargs):
            logging.info("Calling function")
            return wrapped_func(*args, **kwargs)
        return wrap_with_logging(with_logging)
    return wrapped_func