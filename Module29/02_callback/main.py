import functools
from collections.abc import Callable

app = {}


def callback(link: str) -> Callable:
    def func_dec(func: Callable) -> Callable:
        app[link] = func
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper
    return func_dec


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

