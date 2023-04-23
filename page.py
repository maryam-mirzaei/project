import dash
import getFromJsonAndSort
import dash_bootstrap_components as dbc 
import dash_html_components as html 
import webscrap
import json
from kala import kala
import convert_file_to_data
import getFromJsonAndSort
import time

global sortable
sortable=False

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SIMPLEX])
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.H1('جستجو در دیجی کالا', className='text-center')], width=10, style={"height":"100%",'margin-top':'40px'}),
        dbc.Col([ html.Img(src=app.get_asset_url('arm/arm.jpg'),width='150px',height='150px')], width=2, style={"height": "50%"}),
    ],className='text-right',style={'margin-top':'20px'}),
    dbc.Row([
        dbc.Col([
            dbc.Select(id='dropdown',
                    options=[
                        {'label': 'پیشفرض', 'value': 'Default'},
                        {'label': 'قیمت', 'value': 'Price'},
                        {'label': 'امتیاز', 'value': 'Rate'},
                    ],
                    value='Default', className='text-center',style={"width": "50%"}
                ),html.Div(id='output_sort')]),
        dbc.Col([
                dbc.Label(":مرتب کردن بر اساس"),
                ],style={"width": "20%"}),
        dbc.Col(html.Section()),
        dbc.Col([
                html.Button('جستجو', id='searchbtn', n_clicks=0),
                html.Div(id='results'),
                ]),
        dbc.Col([dbc.Input(id="input", value="", type="text",style={'text-align':'right'}),
                ]),
        dbc.Col([html.Label(':جستجو کالا')])
    ]),
])
global mykala
#**************************************
@app.callback(
    dash.dependencies.Output('results', 'children'),
    [dash.dependencies.Input('searchbtn', 'n_clicks')],
    [dash.dependencies.State('input', 'value'),
     dash.dependencies.State('dropdown','value')],
)
# ----------
def search(n_clicks,input,dropdown):
    if n_clicks>0:
        sortable=True
        print('waitting....')
        webscrap.webscrapping(input)
        time.sleep(30)
        getFromJsonAndSort.sort(dropdown)
        
        with open('keyBoard1.json', 'r',encoding='utf-8') as f:
            json_data = json.load(f)

        # Create a list of objects from the JSON data
        kalas = [kala(p['link'], p['img'],p['title'],p['price'],p['rate']) for p in json_data]

        children=drow_table(kalas)
        return children
#*************************************************
@app.callback(
    dash.dependencies.Output('output_sort', 'children'),
    [dash.dependencies.Input('dropdown', 'value')],
    [dash.dependencies.State('input', 'value')],
)
#-----------
def update_output(value,input):
    if input != '' and sortable:
        getFromJsonAndSort.sort(value)
        with open('keyBoard1.json', 'r',encoding='utf-8') as f:
            json_data = json.load(f)

        # Create a list of objects from the JSON data
        kalas = [kala(p['link'], p['img'],p['title'],p['price'],p['rate']) for p in json_data]      
        children=drow_table(kalas)   
        return children
#*************************************************
def drow_table(kalas):

    rows = [html.Tr([html.Th('امتیاز کالا'),html.Th('قیمت'),html.Th('عنوان'),html.Th('تصویر'),])]

    # Create item needed
    price = [item.price for item in kalas]
    title = [item.title  + '\nقیمت:' + str(item.price) for item in kalas]
    link=[item.link for item in kalas]
    imgs =[item.img for item in kalas]
    rate=[item.rate for item in kalas]

    for i in range(len(rate)):
        if rate[i] == -1:
            rate[i]="فاقد امتیاز"
    
    for i in range(len(price)):
        if price[i] == -1:
            price[i]="ناموجود"

    for l,i,t,p,r in zip(link,imgs,title,price,rate):
        img = html.Img(src=i,width='100px',height='100px')
        d = html.Tr([html.Td(r),html.Td(p),html.A(t,href=l),html.Td(img)])
        rows.append(d)
    print('wait more....')
    ch = [html.Table(rows,style={'width':'100%'})]
    return ch

#*************************************************
if __name__=='__main__':
    app.run_server(port='8000')