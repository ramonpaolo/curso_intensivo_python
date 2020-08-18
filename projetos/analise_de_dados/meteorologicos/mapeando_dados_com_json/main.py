import json

filename = "population_data.json"

with open(filename) as file:
    pop_data = json.load(file)

for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        nome_pais = pop_dict["Country Name"]
        try:
            populacao = int(pop_dict["Value"])
        except ValueError:
            #transforma a string em float e o float em inteiro(remove o ponto)
            populacao = int(float(pop_dict["Value"]))
        else:
            print(nome_pais + ": " + str(populacao))