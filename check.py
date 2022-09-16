import json

with open('modification_type_uz_1.json') as data_file:
    data = json.load(data_file)

    print(len(data))
