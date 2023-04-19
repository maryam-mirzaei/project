from dash import Dash, dcc, html, Input, Output
import getFromJsonAndSort
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components
import dash_html_components as html # pip install dash-html-components

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    'مرتب کردن بر اساس:',
    dcc.Dropdown(   options=[
       {'label': 'پیشفرض', 'value': 'Default'},
       {'label': 'قیمت', 'value': 'Price'},
       {'label': 'امتیاز', 'value': 'Rate'},
   ],
   value='Default', id='demo-dropdown'),
    html.Div(id='dd-output-container')
],style={"width": "30vh", "color": "black"})


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    kala=getFromJsonAndSort.sort(value)

if __name__=='__main__':
    app.run_server(port='8000')