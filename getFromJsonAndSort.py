import json
from kala import kala

# Load the list of objects from the JSON file
with open('keyBoard.json', 'r',encoding='utf-8') as f:
    json_data = json.load(f)
# print(json_data)

# Create a list of objects from the JSON data
kalas = [kala(p['link'], p['img'],p['title'],int(p['price'].replace(',', '')),float(p.get('star', 0))) for p in json_data]
for kala in kalas:
    kala_dict = kala.__dict__
    print(kala_dict['price'])
    # print(kala_dict)

# sort by Price ================================================================
kalas.sort(key=lambda x: x.price, reverse=True)
print('sorted:==========================================')
for kala in kalas:
    kala_dict = kala.__dict__
    print(kala_dict['price'])

# sort by star ================================================================
kalas.sort(key=lambda x: x.star, reverse=True)
print('sorted:==========================================')
for kala in kalas:
    kala_dict = kala.__dict__
    print(kala_dict['star'])