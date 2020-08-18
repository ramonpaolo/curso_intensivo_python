from pygal_maps_world.maps import World
import json
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

from countries import get_country

filename = "./mapeando_dados_com_json/population_data.json"

with open(filename) as file:
    pop_data = json.load(file)

cc_population = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        nome_pais = pop_dict["Country Name"]
        #transforma a string em float e o float em inteiro(remove o ponto)
        populacao = int(float(pop_dict["Value"]))
        code = get_country(nome_pais)
        print(nome_pais + ": " + str(populacao))
        cc_population[code] = populacao
        print(cc_population)

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 100000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

py_style = RotateStyle("#336699", base_style=LightColorizedStyle)
py = World(style=py_style)
py._title = "World Population in 2010, by Countrys"
py.add("0-10m", cc_pops_1)
py.add("10-100m", cc_pops_2)
py.add("100-1b", cc_pops_3)

py.render_to_file("World_population.svg")