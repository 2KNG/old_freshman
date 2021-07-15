import json

data = {"id":"01", "language" : {"java":"advance"},
        "edition":"third", "author":"Herberts"}

with open("test.json", "w", encoding='utf-8-sig') as out_file:
    json.dump(data, out_file, indent = 2)
    str_data = json.dumps(data, indent=2)
    print(str_data)
    # dump 는 찍어라는 뜻

print(type(str_data))