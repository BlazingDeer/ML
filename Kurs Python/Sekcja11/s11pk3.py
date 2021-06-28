import os
import zipfile
import requests


class FileFromWeb:
    def __init__(self,url,tmp_file):
        self.url=url
        self.tmp_file=tmp_file

    def __enter__(self):
        response=requests.get(self.url)
        with open(self.tmp_file, "wb") as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type==FileNotFoundError:
            print("Podany Katalog nie istnieje!")
            print(exc_type)
            print(exc_val)
            print(exc_tb)
            return True
        elif exc_type==KeyError:
            print("Podany plik nie znajduje się w zipfile!")
            print(exc_type)
            print(exc_val)
            print(exc_tb)
            return True
        else:
            return False

with FileFromWeb(r"https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip","euroxref.zip") as f:
    with zipfile.ZipFile(f.tmp_file,"r") as z:
        a_file=z.namelist()[0]
        print(a_file)
        os.chdir("./tmpe")
        z.extract(a_file,"./",None)
