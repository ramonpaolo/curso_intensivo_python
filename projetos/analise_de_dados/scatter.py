from matplotlib import pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

#argumento "S" define o tamanho dos pontos no gráfico
#argumento "edgecolor" seria a a cor da borda do ponto
#argumento "C" seria a a cor de dentro do ponto
#plt.scatter(x_values, y_values, s=40, edgecolors="black", c="red")

#Apartir do valor do eixo Y, quando maior for o valor de y, mais escura a cor fica
plt.scatter(x_values, y_values, s=40, edgecolors="none", c=y_values, cmap=plt.cm.Blues)
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Define o intervalo para cada ponto do gráfico(inicio e fim)
#plt.axis([-20, 1100, -20000, 1100000])

#Define o tamanho dos rótulos das marcações
plt.tick_params(axis="both", labelsize=14, which="major")

plt.savefig("squares_plot.png", bbox_inches="tight")