import time
import functools


def CreateFunctionWrapper(func):
    def WrappedFunction(*args,**kwargs):
        print(f"Function '{func.__name__}({args[0]})' is running'")
        time_start=time.time()
        result=func(*args,**kwargs)
        time_stop=time.time()
        print(f"Result = {result}")
        print(f"Function was running for {time_stop-time_start} seconds")
        return result
    return WrappedFunction

@CreateFunctionWrapper
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v

#newFunc=CreateFunctionWrapper(get_sequence)
#newFunc(18)

get_sequence(18)