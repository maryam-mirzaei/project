from dash import Dash, dcc, html, Input, Output
import getFromJsonAndSort
import dash_bootstrap_components as dbc 
import dash_html_components as html 

app = Dash(__name__,external_stylesheets=[dbc.themes.SIMPLEX])
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.H1('جستجو در دیجی کالا', className='text-center')], width=10, style={"height":"100%",'margin-top':'40px'}),
        dbc.Col([ html.Img(src=app.get_asset_url('arm/arm.jpg'),width='150px',height='150px')], width=2, style={"height": "50%"}),

    ],className='text-right',style={'margin-top':'20px'}),

    dbc.Row([
        dbc.Col([
            dbc.Select(
                    options=[
                        {'label': 'پیشفرض', 'value': 'Default'},
                        {'label': 'قیمت', 'value': 'Price'},
                        {'label': 'امتیاز', 'value': 'Rate'},
                    ],
                    value='Default', id='demo-dropdown',className='text-center',style={"width": "50%"}
                )]),
        dbc.Col([
                dbc.Label(":مرتب کردن بر اساس"),
            ],style={"width": "20%"})
    ], className='my-4'),
    html.Div(id='dd-output-container')
])

@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    kala=getFromJsonAndSort.sort(value)
    print(kala)

if __name__=='__main__':
    app.run_server(port='8000')