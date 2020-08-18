import json

filename = "usuarios.json"

try:
    with open(filename) as file:
        nome = json.load(file)

except FileNotFoundError:
    name = input("Digite seu nome: ")

    with open(filename, "w") as file:
        json.dump(name, file)
        print("We'll remeber you when you come back, " + name + "!")

else:
    print("Welcome back, " + nome + "!")