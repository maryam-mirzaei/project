import dash
import getFromJsonAndSort
import dash_bootstrap_components as dbc 
import dash_html_components as html 
import webscrap
import json
from kala import kala
import getFromJsonAndSort
import time
from plot import draw_plot
from draw_table import draw_table

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SIMPLEX])
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.H2('جستجو در دیجی کالا', className='text-center')], width=10, style={"height":"100%",'margin-top':'30px'}),
        dbc.Col([ html.Img(src=app.get_asset_url('arm/arm.jpg'),width='120px',height='120px')], width=2, style={"height": "50%"}),
    ],className='text-right',style={'margin-top':'20px'}),
    dbc.Row([
        dbc.Col([   
        dbc.Card([
            dbc.Row([html.Img(src=app.get_asset_url('img/mobile.jpg'),width='150px',height='150px')],style={"height": "20%"}),
            dbc.Row([html.A('موبایل',href="https://www.digikala.com/search/category-mobile-phone/"),])],style={'margin-top':'30px'},className='text-center'),]),
        dbc.Col([
        dbc.Card([
            dbc.Row([html.Img(src=app.get_asset_url('img/digital-appliances.jpg'),width='150px',height='150px')], style={"height": "20%"}),
            dbc.Row([html.A('کالای دیجیتال',href="https://www.digikala.com/main/electronic-devices/")]),],style={'margin-top':'30px'},className='text-center'),]),
        dbc.Col([
        dbc.Card([
            dbc.Row([html.Img(src=app.get_asset_url('img/home.jpg'),width='150px',height='150px')], style={"height": "20%"}),
            dbc.Row([html.A('خانه و آشپزخانه',href="https://www.digikala.com/main/home-and-kitchen/")]),],style={'margin-top':'30px'},className='text-center'),]),
        dbc.Col([
        dbc.Card([
            dbc.Row([html.Img(src=app.get_asset_url('img/mode.jpg'),width='150px',height='150px')], style={"height": "20%"}),
            dbc.Row([html.A('مد و پوشاک',href="https://www.digikala.com/main/apparel/")]),],style={'margin-top':'30px'},className='text-center'),]),
        dbc.Col([
        dbc.Card([
            dbc.Row([html.Img(src=app.get_asset_url('img/market.jpg'),width='150px',height='150px')], style={"height": "20%"}),
            dbc.Row([html.A('سوپرمارکت',href="https://www.digikala.com/main/food-beverage/")]),],style={'margin-top':'30px'},className='text-center'),]),
        dbc.Col([
        dbc.Card([
            dbc.Row([html.Img(src=app.get_asset_url('img/tahrir.jpg'),width='150px',height='150px')], style={"height": "20%"}),
            dbc.Row([html.A('لوازم التحریر',href="https://www.digikala.com/main/book-and-media/")]),],style={'margin-top':'30px'},className='text-center'),]),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Select(id='dropdown',
                    options=[
                        {'label': 'پیشفرض', 'value': 'Default'},
                        {'label': 'قیمت', 'value': 'Price'},
                        {'label': 'امتیاز', 'value': 'Rate'},
                    ],
                    value='Default', className='text-center',style={"width": "50%"}
                )]),
        dbc.Col([
                dbc.Label(":مرتب کردن بر اساس"),
                ],style={"width": "20%"}),
        dbc.Col(html.Section()),
        dbc.Col([
                html.Button('جستجو', id='searchbtn', n_clicks=0),
                
                ]),
        dbc.Col([dbc.Input(id="input", value="", type="text",style={'text-align':'right'}),
                ]),
        dbc.Col([html.Label(':جستجو کالا')])
    ],style={'margin-top':'40px'}),
    dbc.Row([dbc.Col(id='results')], className='text-center'),
    dbc.Row([dbc.Col(id='show_plot')],style={"width": "100%"})
])

#**************************************
@app.callback(
    [dash.dependencies.Output('results', 'children'),
    dash.dependencies.Output('show_plot','children')],
    [dash.dependencies.Input('searchbtn', 'n_clicks')],
    [dash.dependencies.State('input', 'value'),
     dash.dependencies.State('dropdown','value')],
)
# ----------
def search(n_clicks,input,dropdown):

    if n_clicks>0:
        print('waitting....')

        webscrap.webscrapping(input)
        # thats not required
        # time.sleep(30)

        getFromJsonAndSort.sort(dropdown)
        
        with open('keyBoard1.json', 'r',encoding='utf-8') as f:
            json_data = json.load(f)

        # Create a list of objects from the JSON data
        kalas = [kala(p['link'], p['img'],p['title'],p['price'],p['rate']) for p in json_data]
        
        children=draw_table(kalas)
        children1=draw_plot(kalas)

        return [children,children1]
    else:
        return "",""
#*************************************************
if __name__=='__main__':
    app.run_server(port='8000')