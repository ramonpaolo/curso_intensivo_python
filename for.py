lista = ["Ramon", "João", "Maria"]
#para cada item em lista, mostre. "item" é uma váriavel criada no for e usada a qualquer momento
for item in lista:
    print(item.title() + " parabéns")
    print("I cant't wait to see your next trick," + item.title() + "\n")

print("Thank you, everyone")


for valor in range(1, 5):
    print(valor)


quadrado_perfeito = []
for value in range(1, 11):
    quadrado_perfeito.append(value**2)

print(quadrado_perfeito)

#Abrangência de Lista
quadrado_perfeito = [value**2 for value in range(1, 11)]
print(quadrado_perfeito)

digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digitos)) #menor número
print(max(digitos)) #Maior número
print(sum(digitos)) #Soma deles

#----------------------------------FLAG------------------------------------------

for x in range(1, 10):
    if x == 4:
        break
    else:
        print("Continuando com o break...")

for x in range(1, 10):
    if x == 4:
        continue #Reinicia o Loop
    else:
        print("Continuando com o continue..." + x.__str__())

