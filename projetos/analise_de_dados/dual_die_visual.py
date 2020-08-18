import pygal
from Die import Die

die1 = Die()
die2 = Die()

results = []
for roll_num in range(100):
    result = die1.roll() + die2.roll()
    results.append(result)

#print(results)

#Analisa os resultados
frequencies = []
max_frequencies = die1.num_sides + die2.num_sides
for value in range(1, max_frequencies+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#Visualizar os resultados
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6 + D6", frequencies)
hist.render_to_file("dual_die_visual.svg")