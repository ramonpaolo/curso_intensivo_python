from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("Digite seu nome: ")
    if first == 'q':
        break
    last = input("Digite seu ultimo nome: ")
    if last == 'q':
        break

nome_formatado = get_formatted_name(first, last)
print("Formatado: " + nome_formatado)