#!/usr/bin/env python3


import redis
import uuid
from typing import Union, Optional, Callable, TypeVar
import functools



T = TypeVar("T")



def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs_key, str(args))
        out = method(self, *args, **kwargs)
        self._redis.rpush(
            outputs_key,
            out if isinstance(out, (str, bytes, int, float)) else str(out)
        )
        return out

    return wrapper

def replay(method: Callable) -> None:
    r = method.__self__._redis

    qual = method.__qualname__
    in_key = f"{qual}:inputs"
    out_key = f"{qual}:outputs"

    raw_count = r.get(qual)
    count = int(raw_count) if raw_count else 0
    print(f"{qual} was called {count} times:")

    inputs = r.lrange(in_key, 0, -1)
    outputs = r.lrange(out_key, 0, -1)

    for args_b, out_b in zip(inputs, outputs):
        args_str = args_b.decode("utf-8", errors="replace")
        out_str  = out_b.decode("utf-8", errors="replace")
        print(f"{qual}(*{args_str}) -> {out_str}")


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None) -> Optional[Union[bytes, T]]:
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data
    
    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)

if __name__ == "__main__":
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    replay(cache.store)
