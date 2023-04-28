import dash_html_components as html 

def draw_table(kalas):

    rows = [html.Tr([html.Th('امتیاز',style={"width": "15%"}),html.Th('قیمت',style={"width": "15%"}),html.Th('عنوان',style={"width": "40%"}),html.Th('تصویر',style={"width": "20%"}),html.Th('ردیف',style={"width": "10%"})])]

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
    counter=1
    for l,i,t,p,r in zip(link,imgs,title,price,rate):
        img = html.Img(src=i,width='100px',height='100px')
        d = html.Tr([html.Td(r),html.Td(p),html.A(t,href=l),html.Td(img),html.Td(counter)])
        rows.append(d)
        counter +=1
    print('wait more....')
    ch = [html.Table(rows,style={'width':'100%','margin-top':'30px'})]
    return ch