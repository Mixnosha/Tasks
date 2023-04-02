import requests, json

def count_symbols(url: str) -> dict:
    site = requests.get(url)
    symbols: dict = {}
    for i in site.text:
        if i in symbols: symbols[i] += 1
        else: symbols[i] = 1
    return symbols

url: str = "https://www.python.org"
res: dict = count_symbols(url)
with open('task3.json', 'w') as f:
    json.dump(res, f)
