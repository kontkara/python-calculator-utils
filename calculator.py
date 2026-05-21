def process_and_call_wrapper(func: Callable[[*Any], *Any]) -> Union[Callable[[*Any], *Any], None]:
    ...
    if callable(func) and not check_builtin(func):  
        try:
            result = func(*processed_args)
            validate_return_type(result)
            wrapped_func = lambda *args: wrapper(*args) if len(args) == len(processed_arg_names) else None
        except TypeError as e:
            raise ValueError(f"Incorrect type of arguments for {func.__name__}") from e
    ...

def process_and_call_wrapper_with_hint(func: Callable[[*Any], *Any]) -> Union[Callable[[*Any], *Any], None]:
    return typing.cast(Union[Callable[[*Any], *Any], None], process_and_call_wrapper(func))