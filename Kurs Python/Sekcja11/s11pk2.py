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
        pass

with FileFromWeb(r"https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip","euroxref.zip") as f:
    with zipfile.ZipFile(f.tmp_file,"r") as z:
        a_file=z.namelist()[0]
        print(a_file)
        z.extract(a_file,"./tmp/",None)
