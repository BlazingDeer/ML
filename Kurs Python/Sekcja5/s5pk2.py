import os
from datetime import datetime
import functools




def wrapper_with_log_file(path):
    def create_wrapper_function(func):
        def wrapped_func(*args,**kwargs):
            with open(path,"a") as f:
                f.write("\n")
                f.write("-"*20)
                f.write("\n")
                f.write(f"{datetime.now()} - used function {func.__name__}")
                func_info=f"{func.__name__}({','.join(f'{arg}' for arg in args )}"
                func_info+=f",{','.join(f'{k} = {v}' for k,v in kwargs.items())})"
                f.write(func_info)
            result=func(*args, **kwargs)
            return result
        return wrapped_func
    return create_wrapper_function

@wrapper_with_log_file("./logs/create_file_log.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper_with_log_file("./logs/delete_file_log.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file("./dummyfile1.txt")
delete_file("./dummyfile1.txt")
create_file("./dummyfile2.txt")
delete_file("./dummyfile2.txt")