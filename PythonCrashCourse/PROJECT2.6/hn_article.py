import requests
import json
import os

url="https://hacker-news.firebaseio.com/v0/item/19155826.json"
r=requests.get(url)
r.raise_for_status()

response_dict=r.json()
readable_file="data/readable_hn_data.json"
os.makedirs(os.path.dirname(readable_file),exist_ok=True)
with open(readable_file,"w",) as f:
    json.dump(response_dict,f,indent=4)