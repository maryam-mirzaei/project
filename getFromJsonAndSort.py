def sort(sortitem):
    import json
    from kala import kala

    mykala=[]

    # Load the list of objects from the JSON file
    with open('keyBoard1.json', 'r',encoding='utf-8') as f:
        json_data = json.load(f)

    # Create a list of objects from the JSON data
    kalas = [kala(p['link'], p['img'],p['title'],int(p['price'].replace(',', '')),float(p.get('rate', 0))) for p in json_data]

    # sort by Price ================================================================
    if sortitem=="Price":
        kalas.sort(key=lambda x: x.price, reverse=True)
        for kala in kalas:
            kala_dict = kala.__dict__
            mykala.append(kala_dict)

    # sort by rate ================================================================
    elif sortitem=="Rate":
        kalas.sort(key=lambda x: x.rate, reverse=True)
        for kala in kalas:
            kala_dict = kala.__dict__
            mykala.append(kala_dict)

    # defult (no sorted) ================================================================:
    else:
        for kala in kalas:
            kala_dict = kala.__dict__
            mykala.append(kala_dict)

    mykala=json.dumps(mykala)
    with open('keyBoard1.json', mode='w',encoding='utf-8') as f:
        f.write(mykala)