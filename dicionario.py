alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

print("Your earned: " + str(alien_0["points"]) + " points")

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_1 = {}

alien_1["color"] = "red"
alien_1["points"] = 10
print(alien_1)

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x-position: " + alien_0["x_position"].__str__())

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] += x_increment

print("New x-position: " + alien_0["x_position"].__str__())

nome = {
    "first": "Ramon Paolo",
    "last": "Maran",
    "nickname": "r4deu51"
}
for chave, valor in nome.items():
    #print("keys: " + chave)
    print(chave + " " + valor)
print("\n")
for chave in nome.items():
    print(chave)
print("\n")
for chave in nome.keys(): #Faz com que não precisemos pegar a chave e o valor, pegando assim só um dado do dicionário
    print(chave)
print("\n")
for chave in nome: #Mesma coisa que .keys
    print(chave)

favorite_lenguages = {"ramon": "c", "edward": "javaScript", "josé": "python", "maria": "python"}

friend = ["ramon", "ana", "josé"]
print("\n")
for name in favorite_lenguages.keys():
    print(name.title())
    if name in friend:
        print("Hi " + name.title() + ", I see your favorite lenguage is " + favorite_lenguages[name].title() + "!")
    else:
        print("Haven't")
print("\n")
for name in sorted(favorite_lenguages.keys()):
    print(name.title())
print("\n")
for value in favorite_lenguages.values():
    print(value.title())

print("\n")
for value in set(favorite_lenguages.values()): #Retira o valor duplicado do dicionário
    print(value.title())

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens[0]:
    print(alien)

for alien in range(30):
    novo_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(novo_alien)

for alien in aliens[:5]:
    print(alien)
print("\n O número total de aliens é: " + str(len(aliens)))

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["points"] = 15
        alien["speed"] = "fast"

print(aliens)

pizza = {
    "crust": "thick", # Crosta Grossa
    "toppings": ["mushrooms", "extra cheese"] #Cobertura
}

print("You ordered a " + pizza["crust"] + "-crust pizza" +
" with the following topping: ")

for topping in pizza["toppings"]:
    print(topping)

favorite_lenguages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["go", "ruby"],
    "phil": ["python", "haskell"],
}
for name, languages in favorite_lenguages.items():

    if len(languages) <= 1:
        print("\n" + name.title() + "'s favorite lenguage is:")
    else:
        print("\n" + name.title() + "'s favorite lenguages are:")

    for lenguage in languages:
        print("\t" + lenguage.title())

users = {
    "alberto": {
        "first": "alberto",
        "last": "ainsten",
        "location": "itapeva"
    },
    "rodolfo": {
        "first": "rodolfo",
        "last": "algusto",
        "location": "itabera"
    }
}

for user, user_info in users.items():
    print("Username: " + user.title())
    print("first name: " + user_info["first"].title())
    print("last name: " + user_info["last"].title())
    print("location: " + user_info["location"].title())
    print("name full: " + user.title() + " " + user_info["last"].title() + "\n")


#----------------------------------FLAG------------------------------------------
