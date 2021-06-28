from matplotlib import pyplot as plt
from die import Die

die_1=Die()
die_2=Die()


results=[ die_1.roll()+die_2.roll() for roll_num in range(50000)]

max_result=die_1.num_sides+die_2.num_sides
frequencies=[results.count(value) for value in range(2, max_result+1)]

#visualize the results
x_values=list(range(2,max_result + 1))

plt.bar(x_values,frequencies)
plt.xlabel("Results")
plt.ylabel("Count of results")
plt.title("Results of throwing two D6 dice 50000 times.")
plt.xticks(x_values,x_values)
plt.show()