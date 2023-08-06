def decorator_with_args_for_any_decorator(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func, *args, **kwargs):
    def dec_func(func):
        def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                return result
        return wrapper
    return dec_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
decorated_function("Юзер", 101)  # TODO видите, второй вызов фукнции уже не выводит параметры декоратора, так как сейчас
                                 #  их вывод делается во время декорирования, а не в момент вызова функции


# TODO Вот так будет правильно:
from typing import Callable, Optional, Any
import functools


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:  # TODO тут через параметр передаётся декорируемый декоратор
    """ Декоратор. Даёт возможность другому декоратору принимать произвольные аргументы """
    def decorator_maker(*args, **kwargs) -> Callable:  # TODO тут передаются параметры декоратора
        def decorator_wrapper(func: Callable) -> Callable:  # TODO а это декорируемая функция
            return decorator_to_enhance(func, *args, **kwargs)  # TODO возвращается декорированная с помощью decorator_to_enhance функция
        return decorator_wrapper  # TODO возвращается декорированный декоратор
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    """ Декоратор. Шаблон """
    @functools.wraps(func)
    def wrapper(function_arg1: Optional[Any], function_arg2: Optional[Any]) -> Callable:
        print("Переданные арги и кварги:", args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """ Пример декорируемой функции """
    print("Привет", text, num)


decorated_function("Юзер", 101)
