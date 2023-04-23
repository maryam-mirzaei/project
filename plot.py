from dash import Dash, dcc
import dash_bootstrap_components as dbc 
import json
from kala import kala

# for plotting =================================================
import plotly.graph_objects as go

app = Dash(__name__,external_stylesheets=[dbc.themes.SIMPLEX])

# Load the list of objects from the JSON file
with open('keyBoard.json', 'r',encoding='utf-8') as f:
    json_data = json.load(f)

# Create a list of objects from the JSON data
kalas = [kala(p['link'], p['img'],p['title'],int(p['price'].replace(',', '')),float(p.get('rate', 0))) for p in json_data]


# Create item needed
prices = [item.price for item in kalas]
title = [item.title  + '\nقیمت:' + str(item.price) for item in kalas]

# create trace object
trace = go.Scatter(
# item number on x axis
    x=list(range(1, len(kalas)+1)),
# item point on y axis
    y=prices,
# defin mode
    mode='lines',
    name='Data',
# for show whats show when on point
    hoverinfo='text',
)
# for hover show text
trace.text = title
# Create the layout
layout = go.Layout(
# for plot area color
    template='plotly_dark'
)

# Create the figure object
fig = go.Figure(data=[trace], layout=layout)
# title_x for positioning title 
fig.update_layout(legend_title_text = 'نمودار قیمت',title_x=0.5)
fig.update_xaxes(title_text="شماره کالا")
fig.update_yaxes(title_text="قیمت کالا")
graph = dcc.Graph(id='plot', figure=fig)


app.layout = dbc.Container([graph])

if __name__=='__main__':
    app.run_server(port='8000')