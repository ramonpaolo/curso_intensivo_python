import json

numeros = [1, 2, 5, 7, 11, 13]

filename = "numeros.json"
with open(filename, "w") as file:
    json.dump(numeros, file)

with open(filename) as file:
    numbers = json.load(file)
    
print(numbers)