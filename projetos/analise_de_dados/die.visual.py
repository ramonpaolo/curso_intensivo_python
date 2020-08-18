import pygal
from Die import Die

die = Die()

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

#print(results)

#Analisa os resultados
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#Visualizar os resultados
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")