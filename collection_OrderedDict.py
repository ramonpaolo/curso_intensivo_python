#Lista Ordenada

from collections import OrderedDict

favorite_lenguages = OrderedDict()
favorite_lenguages["Ramon"] = "Python"
favorite_lenguages["Dudu"] = "Python"
favorite_lenguages["Danilo"] = "Java"
favorite_lenguages["enzo"] = "JavaScript"

for nome, linguagen in favorite_lenguages.items():
    print(nome.title() + " gosta da linguagem: " + linguagen)
