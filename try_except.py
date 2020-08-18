try:
    print(5/0) #tente, se não conseguir, vá para o de baixo
except ZeroDivisionError:
    print("You can't divide by zero!")

print("give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("Digite numero: ")
    if first_number == 'q':
        break

    second_number = input("Digite segundo numero: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("Não dívisivel por 0")

    else: #Se o try conseguir rodar, então roda o else
        print(answer)