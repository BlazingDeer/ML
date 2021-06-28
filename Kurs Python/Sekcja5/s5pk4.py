import time
import functools

@functools.lru_cache()
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start=time.time()
for i in range(100):
    fib(i)
end=time.time()

print(f"Execution time {end-start}s")
print(fib.cache_info())