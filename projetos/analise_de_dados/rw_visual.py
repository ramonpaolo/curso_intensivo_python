import matplotlib.pyplot as plt
from randowm_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)

#Marca o primeiro ponto
plt.scatter(0, 0, s=100, edgecolors="black")

#Marca o ultimo ponto
plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, edgecolors="black")

plt.figure(dpi=168, figsize=(10, 6))
plt.show()

#Desativa o eixo X e Y
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)