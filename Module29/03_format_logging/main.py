import functools
import time
from datetime import datetime
from typing import Callable


def dec_method(func, class_name, time_format):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_format_time = ''
        for i in time_format:
            if i.isalpha():
                new_format_time += f'%{i}'
            else:
                new_format_time += i
        start = time.time()
        print(f'Запускается "{class_name}.{func.__name__}". Дата и время запуска: '
              f'{datetime.utcnow().strftime(new_format_time)}')
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Завершение {class_name}.{func.__name__}: , {round(end - start,3)}sec')
        return result
    return wrapper


def log_methods(time_format):
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorator_method = dec_method(cur_method, cls.__name__, time_format)
                setattr(cls, i_method_name, decorator_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
