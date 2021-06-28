import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.e'
dir = './temp'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    save_url_to_file(url,tmpfile_path)
    shutil.move(tmpfile_path,file_path)
except requests.exceptions.ConnectionError as e:
    print(f"Invalid url: {url}\nDetails:\n {e}")
except PermissionError as e:
    print(f"File {file_path} is readonly.\nDetails:\n{e}")
except FileNotFoundError as e:
    print(f"File has not been found.\nDetails:\n{e}")
except Exception as e:
    print(f"An Error occured - Details: {e}")
else:
    print("Download finshed succesfully!")
finally:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
