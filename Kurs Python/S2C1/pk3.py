wybory=["load data", "export data","analyze & predict"]
wybor=input()
while wybor:
    if wybor is not int:
        print(type(wybor))
    elif wybor in range(len(wybory)):
        print(wybory[wybor])
    else:
        print("wybor niepoprawny")
    wybor=input()