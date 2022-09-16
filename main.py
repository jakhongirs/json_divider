import json


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


with open('modification_type _uz.json') as data_file:
    data = json.load(data_file)

    sorted_data = list(split(data, 3))

    with open('modification_type_uz_1.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_data[1], f, ensure_ascii=False, indent=4)
