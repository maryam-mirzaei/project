def sort(sortitem):
    import json
    from kala import kala

    # Load the list of objects from the JSON file
    with open('keyBoard.json', 'r',encoding='utf-8') as f:
        json_data = json.load(f)
    print(json_data)

    # Create a list of objects from the JSON data
    kalas = [kala(p['link'], p['img'],p['title'],int(p['price'].replace(',', '')),float(p.get('rate', 0))) for p in json_data]
    for kala in kalas:
        kala_dict = kala.__dict__

    # sort by Price ================================================================
    if sortitem=="Price":
        kalas.sort(key=lambda x: x.price, reverse=True)
        for kala in kalas:
            kala_dict = kala.__dict__
        return kala_dict

    # sort by rate ================================================================
    elif sortitem=="Rate":
        kalas.sort(key=lambda x: x.rate, reverse=True)
        for kala in kalas:
            kala_dict = kala.__dict__
        return kala_dict
    # defult (no sorted) ================================================================
    else:
        return kala_dict