from datetime import datetime
def create_function(format="d"):
    divide_by=1
    if format=="d":
        divide_by=86400
    elif format=="h":
        divide_by=3600
    else:
        divide_by=60

    source="""
def func(start, end):
    duration = end - start
    dur_in_s = duration.total_seconds()
    return dur_in_s/{}
""".format(divide_by)
    exec(source,globals())
    return func

start = datetime(2019, 1, 1, 0, 0, 0)
end  = datetime.now()
f1=create_function("d")
f2=create_function("h")
f3=create_function("m")

print(f1(start,end))
print(f2(start,end))
print(f3(start,end))
