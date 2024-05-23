import json

with open('countries.json') as f:
    data = json.load(f)

print(type(data))