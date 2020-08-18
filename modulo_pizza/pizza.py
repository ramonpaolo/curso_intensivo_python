def make_pizza(size, *toppings):
    print("O tamanho da pizza será de: " + str(size))
    print("Os sabores são: ")
    for topping in toppings:
        print("- " +  str(topping))