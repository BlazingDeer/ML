import requests
import os
import functools


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
dir = './html'
file = 'spis.html'
save_url_to_dir=functools.partial(save_url_file,dir=dir,msg=msg)
save_url_to_dir(url=url,file=file)

