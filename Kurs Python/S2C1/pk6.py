import os
import urllib.request

data_dir="./html/"
pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pages:
    path=data_dir+page["name"]+".html"
    try:
        r=urllib.request.urlretrieve(page["url"],path)
    except Exception as e:
        print(e)
        break
else:
    print("udalo sie pobrac wszystkie strony!")