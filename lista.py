name = " Ramon   "
bicicletas = ["minha", "dele", "alguma marca"]
print(bicicletas)
print(name.strip() + " andou na " + bicicletas[0].title())

bicicletas.append("Honda")
print(bicicletas)

bicicletas.insert(0, "Zero")
print(bicicletas)

#Utilize del quando quiser apagar um item da lista e pop quando quiser utilizar o item apagado

del bicicletas[0]
print(bicicletas)

pop_bicicletas = bicicletas.pop()
print(bicicletas)
print(pop_bicicletas)

pop_bicicletas = bicicletas.pop(1)
print(pop_bicicletas)

bicicletas.append("Honda")
bicicletas.append("Yamaha")
print(bicicletas)

bicicletas.remove("Honda")
print(bicicletas)

#bicicletas.sort()   #Ordena
#print(bicicletas)

#bicicletas.sort(reverse=True)
#print(bicicletas)

print("\nAqui está a lista original: \t" + str(bicicletas) + "\n")
print("E aqui as alfabéticas:\t" + str(sorted(bicicletas))) #Ordena por um momento a lista
print("\nAqui está a lista original: \t" + str(bicicletas) + "\n")

bicicletas.append("teste")
bicicletas.reverse()        #Ele não deixa em ordem alfabética inversa, somente inverte a ordem
print(bicicletas)

bicicletas.reverse() #Para reverter novamente

print(len(bicicletas))

print(bicicletas[-1])

#----------------------------

numeros = list(range(1, 6))
print(numeros)

numeros = list(range(2, 11, 2)) #Começa em 2 e pula em 2 até 11
print(numeros)

players = ["ramon", "josé", "charles", "nicolas", "matheus"]
print(players[0:2])
print(players[:3]) #Fatia os 3 primeiros e mostra eles
print(players[-3:]) #Fatia os 3 ultimos e mostra eles
print(players[3:]) #Fatia os 3 primeiros e mostra os 2 ultimos

primeiros_jogadores = players[0:6:2]
print(primeiros_jogadores)

for nomes in players[-3:]:
    print(nomes.title() + ", Game Over")

comida_preferida = ["Pizza", "Hamburguer", "x-salada", "batata frita"]
amigo_comida = comida_preferida[:3]
print(amigo_comida)
