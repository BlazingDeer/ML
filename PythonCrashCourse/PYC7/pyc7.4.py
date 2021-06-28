import json

filename = "fav_num.json"
try:
    with open(filename) as f:
        fav_num = json.load(f)
except FileNotFoundError:
    print("Enter your favourite number: ")
    while True:
        try:
            fav_num = input()
            fav_num = int(fav_num)
        except ValueError:
            print("It has to be a number: ")
        else:
            break
    with open(filename,"w") as f:
        json.dump(fav_num,f)
else:
    print(f"I know your favourite number, it's {fav_num}")
