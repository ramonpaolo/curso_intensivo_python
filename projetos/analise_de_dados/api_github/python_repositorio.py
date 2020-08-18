import requests
import pygal

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)

#Se voltar com valor de 200 signifac que tudo ok
print("Status code: ", r.status_code)

#Transforma o JSON em Lista
response_dict = r.json()
print("Total de repositórios Python: ", response_dict["total_count"])

repo_dicts = response_dict["items"]
print("Repositorios retornados: ", len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))

for key in sorted(repo_dict.keys()):
    print(key)

plot_dics = []
names = []
#stars = []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    #stars.append(repo_dict["stargazers_count"])

    plot_dic = {
        "value": repo_dict["stargazers_count"],
        "label": repo_dict["description"] or "",
        "xlink" : repo_dict["html_url"]
    }
    plot_dics.append(plot_dic)

    print("\nName: ", repo_dict["name"])
    print("\nOwner: ", repo_dict["owner"]["login"])
    print("\nStars: ", repo_dict["stargazers_count"])
    print("\nRepository: ", repo_dict["html_url"])
    print("\nCreated: ", repo_dict["created_at"])
    print("\nUpdated: ", repo_dict["updated_at"])
    print("\nDescription: ", repo_dict["description"])


py_config = pygal.Config()
py_config.x_label_rotation = 45
py_config.show_legend = False
py_config.title_font_size = 24
py_config.label_font_size = 14
py_config.major_label_font_size = 18
py_config.truncate_label = 15
py_config.show_y_guides = False
py_config.width = 1000

                          #Movimenta o label_x e tira a legenda
py = pygal.Bar(py_config) #show_legend=False, x_label_rotation=45

py._title = "Stars in Projects in GitHub"
py.add("", plot_dics)
#py.add("", stars)
py.x_labels = names

py.render_to_file("python_repositorio.svg")

print(response_dict.keys())