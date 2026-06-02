from typing import Any, Callable, Union, Tuple, Dict

import functools

processed_args: Any
processed_arg_names: Tuple[Any, ...]
_init_checked: bool = False  # added this variable for process_and_call_wrapper_with_hint to check initialization

func_metadata: Dict[str, str] = {}  # new metadata dictionary for function info

def get_func_name(func: Callable[[*Any], *Any]) -> str:
    return func.__name__ if callable(func) else "Unknown"

def process_and_call_wrapper(func: Callable[[*Any], *Any]) -> Union[Callable[[*Any], *Any], None]:
    if callable(func):
        _validate_processable(func)
        try:
            result = func(*processed_args)
            validate_return_type(result)
            wrapped_func = lambda *args: wrapper(*args) if len(args) == len(processed_arg_names) else None
        except TypeError as e:
            raise ValueError(f"Incorrect type of arguments for {get_func_name(func)}") from e
    return wrapped_func

def process_and_call_wrapper_with_hint(func: Callable[[Tuple[Any, ...]], Tuple[Any, ...]]) -> Union[Callable[[Tuple[Any, ...]], Tuple[Any, ...]], None]:
    if not _init_checked:
        check_initialized()
    __check_args_len(func)
    return process_and_call_wrapper(func)

def validate_processed_args() -> None:
    if processed_arg_names and processed_args and len(processed_arg_names) != len(processed_args):
        raise ValueError("processed_args and processed_arg_names must have the same length")

def wrapper(*args: Tuple[Any, ...]) -> Any:
    return args

def _validate_processable(func: Callable[[*Any], *Any]) -> None:
    if not isinstance(func, (Callable, type)):
        raise TypeError(f"Invalid function {func}")

def check_initialized() -> None:
    global _init_checked
    _init_checked = True

def validate_return_type(result: Any) -> None:
    if result is not None and not isinstance(result, tuple):
        raise ValueError(f"Unexpected return type for {get_func_name(func)}")

def __check_args_len(func: Callable[[Tuple[Any, ...]], Tuple[Any, ...]]) -> None:
    if len(processed_arg_names) != len(func.__code__.co_varnames[1:]):
        raise ValueError("processed_arg_names must match the function's argument names")

def __get_arg_names(func: Callable[[Tuple[Any, ...]], Tuple[Any, ...]]) -> Tuple[Any, ...]:
    return tuple(v.name for v in func.__code__.co_varnames[1:])

def get_processed_arg_names() -> Tuple[Any, ...]:
    if processed_arg_names:
        return processed_arg_names
    else:
        raise ValueError("processed_arg_names is not initialized")

def __set_processed_arg_names(func: Callable[[Tuple[Any, ...]], Tuple[Any, ...]]) -> None:
    global processed_arg_names
    processed_arg_names = __get_arg_names(func)

def get_func_arg_names(func: Callable[[*Any], *Any]) -> Tuple[Any, ...]:
    return tuple(arg.name for arg in func.__code__.co_varnames[1:])

def __validate_input(func: Callable[[Tuple[Any, ...]], Tuple[Any, ...]]) -> None:
    if not callable(func):
        raise TypeError(f"{func} is not a valid function")

process_and_call_wrapper = functools.partial(process_and_call_wrapper, validate_processed_args)

def __check_func_return_type(func: Callable[[], Any]) -> None:
    try:
        result = func()
        if result is not None and not isinstance(result, tuple):
            raise ValueError(f"Unexpected return type for {get_func_name(func)}")
    except Exception as e:
        raise ValueError(f"Error calling function {get_func_name(func)}: {e}")

def __set_initial_checked() -> None:
    global _init_checked
    _init_checked = True

check_initialized = __set_initial_checked

def __process_and_call_wrapper_with_hint(func: Callable[[Tuple[Any, ...]], Tuple[Any, ...]]) -> Union[Callable[[Tuple[Any, ...]], Tuple[Any, ...]], None]:
    if not callable(func):
        raise TypeError(f"{func} is not a valid function")
    return process_and_call_wrapper(func)

def get_func_metadata(func: Callable[[*Any], *Any]) -> Dict[str, str]:
    if func.__name__ in func_metadata:
        return func_metadata[func.__name__]
    else:
        raise ValueError(f"Function {get_func_name(func)} has no metadata")