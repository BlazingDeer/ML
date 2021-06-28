import json

filename="data/earthquakes_25_09_2020-02_10_2020.geojson"
with open(filename,encoding='utf-8') as f:
    eq_data=json.load(f)

save_filename="data/earthquakes_25_09_2020-02_10_2020_readable.geojson"
with open(save_filename, "w") as f:
    json.dump(eq_data,f,indent=4)