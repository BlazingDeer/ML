import math
import numpy as np

argument_list=list(np.arange(0,10,0.1))

formula=input("Napisz wzor: ")
for x in argument_list:
    result=eval(formula)
    print(result)

