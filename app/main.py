from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, tuple(kwargs.items()))
        if key not in result:
            print("Calculating new result")
            result2 = func(*args, **kwargs)
            result[key] = result2
            return result2
        else:
            print("Getting from cache")
            return result[key]
    return wrapper


@cache
def long_time_func(base: int, exponent: int, power: int) -> int:
    return (base ** exponent ** power) % (base * power)


print(long_time_func(1, 2, 3))
print(long_time_func(2, 2, 3))
print(long_time_func(1, 2, 3))
