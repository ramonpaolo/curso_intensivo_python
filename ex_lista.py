paises = ["eua", "canadá", "alemanha", "japão", "china"]
print(paises)
print(sorted(paises))
print(paises)
print(sorted(paises, reverse=True))
print(paises)
paises.reverse()
print(paises)
paises.reverse()
print(paises)
paises.sort()
print(paises)
paises.sort(reverse=True)
print(paises.__str__() + "\n\n\n")

#----------------------------------------------------------

lugares = ["Rio taquari", "itai", "itapeva", "toronto", "canadá", "itaberá"]
lugares.append("taquarivai")

print(sorted(lugares))
print(sorted(lugares, reverse=True))
print(lugares[0].title())
lugares.reverse()
print(lugares)
lugares.reverse()
print(lugares)
lugares.sort(reverse=True)
print(lugares)
lugares.sort()
print(lugares)

mercado = ["batata", "arroz", "feijão", "salada", "pimenta", "mandioca"]

for item in mercado[:3]:
    print(item.title() + " deve ser comprado")
print("\n")
for item in mercado[2:5]:
    print(item.title() + " deve ser comprado")
print("\n")
for item in mercado[-3:]:
    print(item.title() + " deve ser comprado")