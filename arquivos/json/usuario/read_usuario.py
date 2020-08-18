import json

with open("usuarios.json") as file:
    nome = json.load(file)
    print("Welcome back, " + nome + "!")