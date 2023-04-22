def convert_files_to_json():
    data =[]
    with open('title.txt',mode='r',encoding='utf-8') as f:
        title = f.read().split('\n')
    with open('price.txt',mode='r',encoding='utf-8') as f:
        price = f.read().split('\n')
    with open('link.txt',mode='r',encoding='utf-8') as f:
        link = f.read().split('\n')
    with open('img.txt',mode='r') as f:
        img = f.read().split('\n')
    with open('rate.txt',mode='r',encoding='utf-8') as f:
        rate = f.read().split('\n')

    for l,i,t,p,r in zip(link,img,title,price,rate):
        d = {'link':l,'img':i,'title':t,'price':p,'rate':r}
        print('d: ',str(d))
        data.append(d)

    data=str(data)

    with open('keyBoard1.json', mode='w',encoding='utf-8') as f:
        f.write(data)