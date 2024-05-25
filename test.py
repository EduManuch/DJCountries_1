import json

with open('countries.json') as f:
    data = json.load(f)

langs = set()
for item in data:
    for lang in item['languages']:
        langs.add(lang)

langs = list(langs)
langs.sort()
print(langs)
