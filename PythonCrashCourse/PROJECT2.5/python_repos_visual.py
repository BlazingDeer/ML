import plotly.graph_objs as go
from plotly import offline
import requests

# make an api call and store the response

url="https://api.github.com/search/repositories?q=language:python&sort=stars"
headers={"Accept":"application/vnd.github.v3+json"}
r=requests.get(url=url,headers=headers)
print(f"Status code: {r.status_code}")
response_dict=r.json()
print(f"Total repositories: {response_dict['total_count']}")

repo_dicts=response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

repo_links, stars, labels= [], [], []
for repo_dict in repo_dicts:
    repo_name=repo_dict["name"]
    repo_url=repo_dict["html_url"]
    owner = repo_dict["owner"]["login"]
    description=repo_dict["description"]

    repo_link=f"<a href='{repo_url}'> {repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict["stargazers_count"])
    label=f"{owner} <br /> {description}"
    labels.append(label)


data=[go.Bar(x=repo_links
             ,y=stars,
             hovertext=labels,
             marker={
                 "color": "rgb(60,100,150)",
                 "line":{"width":1,"color":"rgb(25,25,25)"}
             },
             opacity=0.6)]
my_layout=go.Layout(title="Stars of most popular repos on GitHub",
                    xaxis={"title":"Repository"},
                    yaxis={"title":"Stars"},
                    titlefont={"size":28})
fig=go.Figure(data=data,layout=my_layout)
offline.plot(fig,filename="python_repos_stars.html")