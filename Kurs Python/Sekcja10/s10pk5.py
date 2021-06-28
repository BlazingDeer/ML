import os
import itertools as it

def scantree(path):
    for element in os.scandir(path):
        if element.is_dir():
            yield element
            yield from scantree(element.path)
        else:
            yield element

path="D:\Programowanie C itp\PYTHON\pycharm\KursDlaSrednioZaaw\Sekcja10"
listing=[]
for element in scantree(path):
    listing.append(element)

for element in listing:
   print(f"{element.path} - is_dir = {element.is_dir()}")

listing=sorted(listing,key=lambda x: x.is_dir())

for key,elements in it.groupby(listing, key=lambda e: e.is_dir()):
    print(f"is_dir={key}, count={len(list(elements))}")