pizza = ["calabresa", "portuguessa", "brigadeiro"]

print("Nós temos os seguintes sabores de pizza: ")

for sabor in pizza:
    print("Sabor: " + sabor.title())

print("\n Pizza é bom dimais. \n Principalmente o de calabresa e portuguessa \n"
      " Ótimo para comer com os amigos \n Pizza melhor comida desse mundooo!!\n")


animais = ["Macaco", "Humano", "leão"]

for animal in animais:
    print("Um " + animal.title() + " seria um ótimo amigo :)")

print("\nEsses animais são ferozes quando se mexe com o bando deles!\n")

lista = []
for value in range(1, 1000001):
    lista.append(value)
print(min(lista))
print(max(lista))
print(sum(lista))
print(len(lista))

for value in range(0, 21, 3):
    print(value)

lista = []
for value in range(0, 31, 3):
    lista.append(value)
print(lista)

for value in range(1, 11):
    print(value**3)

lista = [value**3 for value in range(1, 11)]
print(lista)
print(len(lista))