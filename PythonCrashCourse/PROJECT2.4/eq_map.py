import json
import plotly.graph_objs as go
from plotly import offline

eq_filename = "data/earthquakes_25_09_2020-02_10_2020.geojson"
with open(eq_filename, encoding="utf-8") as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

magnitudes, longitutes, latitudes, titles = [], [], [], []

for eq_dict in all_eq_dicts:
    magnitudes.append(eq_dict["properties"]["mag"])
    titles.append(eq_dict["properties"]["title"])
    longitutes.append(eq_dict["geometry"]["coordinates"][0])
    latitudes.append(eq_dict["geometry"]["coordinates"][1])

fig = go.Figure(data=go.Scattergeo(
    lon=longitutes,
    lat=latitudes,
    text=titles,
    marker={
        "size": [0.15 * mag ** 3 for mag in magnitudes],
        "color": magnitudes,
        "colorscale": "Bluered",
        "colorbar": {"title": "Magnitude"}

    }
))

my_layout = go.Layout(title="Trzęsienia ziemi od 25.09-02.10.2020", geo={
    "showcountries": True
    #,"projection": {"type": "orthographic"}

})
fig.update_layout(my_layout)

offline.plot(fig, filename="trzesienia_ziemi_25_09_do_02_10_2020.html")
