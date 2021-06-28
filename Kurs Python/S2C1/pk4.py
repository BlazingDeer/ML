import os

path="./plik.txt"

with open(path,"w") as f:
    f.write("Ciemnosc widze za oknem i wgl")

def fun(path):
    with open(path,"r") as f:
        text=f.read()
    ilosc_slow=len(text.split())
    print("Ilosc slow:",ilosc_slow)

result=os.path.isfile(path) and fun(path)
