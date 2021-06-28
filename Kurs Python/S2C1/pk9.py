banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
dict_denominations=dict(zip(banknotes_coins,[0 for i in range(len(banknotes_coins))]))

for key,value in dict_denominations.items():
    print(f"dict_denominations[{key}] = {value}")