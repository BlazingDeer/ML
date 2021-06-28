import plotly.graph_objs as go
from plotly import offline
from random_walk import RandomWalk

# Make random walk.
rw = RandomWalk(5000)
rw.fill_walk()

data=[go.Scatter(x=rw.x_values,y=rw.y_values,mode="markers")]
x_axis_config={"showgrid":False,"visible":False,}
y_axis_config={"showgrid":False,"visible":False}
my_layout=go.Layout(title="Random Walk",xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({"data":data,"layout":my_layout},filename="rw.html")
