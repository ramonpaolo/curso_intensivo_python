with open("pi.txt") as file:
    contents = file.read()
    print(contents)

print("\n")

with open("pi.txt") as file:
    for linha in file:
        print(linha)

print("\n")

with open("pi.txt") as file:
    linhas = file.readlines()
    for linha in linhas:
        print(linha.rstrip())

pi = ""
with open("pi.txt") as file:
    linhas = file.readlines()
    for linha in linhas:
        pi += linha.rstrip()

#birthday = input("Digite sua idade: ")
#if birthday in pi:
    print("Tem")
#else:
    print("Não tem")

filename = "programming.txt"

#Irá criar um arquivo se não existir e no modo escrita
with open(filename, "w") as file:
    file.write("I love programming. \n")
    file.write("I love creating new games. \n")

#a seria para adicionar sem criar ou apagar o arquivo(append(adiciona por último))
with open(filename, "a") as file:
    file.write("I also love finding meaning in large datasets. \n")
    file.write("I love creating apps that can run in a browser. \n")

try:
    with open("alice.txt", encoding="UTF-8") as file:
        arquivo = file.read()

except FileNotFoundError:
    print("Arquivo não encontrado")

else:
    print(arquivo)

title = "Alice in Worderland"
print(title.split())

try:
    with open("pass.txt") as file:
        arquivo = file.read()

except FileNotFoundError:
    pass #Simplesmente ignora e não faz nada com o erro

else:
    print(arquivo)