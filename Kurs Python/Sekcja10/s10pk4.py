import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for combination in it.product(notes, repeat=4):
    print(combination)


#num_candidates= math.factorial(len(notes))/math.factorial(len(notes)-4)
num_candidates=pow(len(notes),4)
print(num_candidates)



