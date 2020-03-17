import json

# JSON
with open('Другие.json', 'r') as f:
    special_offers = json.load(f)

print(f'JSON:\n{special_offers}')
print(type(special_offers))
