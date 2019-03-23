import functools

@functools.lru_cache(maxsize=None)
def fib(i):
    if i < 2:
        return 1
    return fib(i - 1) + fib(i - 2)

@functools.lru_cache(maxsize=None)
def C(n,k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    return C(n-1,k-1) + C(n-1,k)

