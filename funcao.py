def diga_ola(username):
    """
    Ele Irá dizer olá
    """
    print("Hello " + username.title())

diga_ola("Ramon")

#-----------------------------------------------------------------------------------------------------------------------

def planejamento():
    print("""
    Estou planejando a criar funções para logo poder iniciar na Machine Learning
    e assim fazer meu caminho como um grande programador
    """)

planejamento()

#-----------------------------------------------------------------------------------------------------------------------

def animal(tipo, nome):
    print("I have a " + tipo + ".")
    print("My " + tipo + " name is " + nome.title() + ".")

animal("Cachorro", "Pit")

#Keyword argument serve para não confundir na hora de passar os parametros
animal(tipo="Cachorro", nome="Pit")

#Valor default
def describe_pet(nome, tipo="Cachorro"):
    print("My " + tipo + " have the name of " + nome.title())

describe_pet(nome="Pit")

#-----------------------------------------------------------------------------------------------------------------------

def get_formated_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

print(get_formated_name("Ramon Paolo", "maran"))

def get_formated_name(first_name, last_name,  middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " +last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

print(get_formated_name("ramon", "maran", "paolo"))

#-----------------------------------------------------------------------------------------------------------------------

def build_person(first_name, last_name, age=""):
    person = {"name": first_name, "last": last_name}
    if age:
        person['age'] = age
    return person

print(build_person("Ramon", "Maran", age=17))

#-----------------------------------------------------------------------------------------------------------------------

while True:
    nome = input("Digite seu primerio nome: ")
    nome_last = input("Digite seu ultimo nome: ")

    print(build_person(first_name=nome, last_name=nome_last))

    continuar = input("Deseja parar? [yes/no]: ")
    if continuar == "yes":
        break

#-----------------------------------------------------------------------------------------------------------------------
def usuarios(nome):
    for name in nome:
        print(name + ", Hello")

usuario = ["Ramon", "Dudu", "Maria"]
usuarios(usuario)

#-----------------------------------------------------------------------------------------------------------------------

unprinted_designs = ["Iphone Case", "Robot Pendant", "Dodecahedron"]
completed_models = []

def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_design = unprinted_models.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe Following models have been printed: ")
    for completed_models in completed_models:
        print(completed_models)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#Faz com que a função não mude a lista original, e sim crie uma cópia
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#-----------------------------------------------------------------------------------------------------------------------

#Numero de argumentos arbitrário
def make_piza(size, *toppings):
    print("O tamanho é: " + str(size))
    print("Os ingredientes são: ")
    for topping in toppings:
        print("- " + topping)

make_piza(12, "Peperoni", "Extra Chessa", "keijo")

#Argumentos arbitrários (se cria depois quantos você quiser)
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("Ramon Paolo", "Maran", localization="Itapeva", age=17)
print(user_profile)