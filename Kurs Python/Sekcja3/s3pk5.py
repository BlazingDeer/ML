import math
import time

formulas_list=["abs(x**3 - x**0.5)", "abs(math.sin(x) * x**2)" ]

argument_list=[]
for i in range(1000000):
    argument_list.append(i/10)



for formula in formulas_list:
    results_list = []
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    stop=time.time()
    print(stop-start)

for formula in formulas_list:
    results_list = []
    start = time.time()
    compiled_formula=compile(formula,"internal variable source","eval")
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    stop=time.time()
    print(stop-start)
