import json

with open('abc.json','r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # Dessa forma o arquivo dentro do json volta ser dicionário

# Para vizualizar o dicionário
for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)