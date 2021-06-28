import os
import requests

def gen_get_files(dir):
    files=os.listdir(dir)
    for file in files:
        yield os.path.join(dir,file)

def gen_get_file_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line

def check_webpage(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        return True
    except:
        return False

try:
    os.mkdir('./links_to_check')
except:
    pass

with open('./links_to_check/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open('./links_to_check/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

for file in gen_get_files("./links_to_check/"):
    for line in gen_get_file_lines(file):
        line=line.rstrip()
        print(file,"-",line,"-",check_webpage(line))