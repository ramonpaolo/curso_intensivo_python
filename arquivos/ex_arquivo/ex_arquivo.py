while True:
    print("Iremos começar")
    nome = input("Digite seu nome: ")
    with open("usuarios.txt", "a") as file:
        file.writelines(nome + "\n")
    continuar = input("Deseja continuar?[yes/no]: ")
    if continuar == "yes":
        continue
    else:
        break

