import functools
import time
from typing import Callable, Any

# Factory for decorators that counts total execution time
def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> Any:
            print(f'starting {func} with args {args} kwargs {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'finished {func} in {total:.4f} s')

        return wrapped
    return wrapper