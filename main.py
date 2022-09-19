import json


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def main(jsonfile, n, filename):
    with open(jsonfile) as f:
        data = json.load(f)

    # Split data into 3 chunks
    chunks = list(split(data, n))

    # Write chunks to files
    for i, chunk in enumerate(chunks):
        with open(f'{filename}_{i}.json', 'w', encoding='utf-8') as f:
            json.dump(chunk, f, ensure_ascii=False, indent=4)


main('modification_type.json', 20, 'modification_type')
