import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "./ehmatthes-pcc-v1.0.0-12-gf555082/sitka_weather_07-2014.csv"

with open(filename) as f:
    ler = csv.reader(f)
    cabecalho = next(ler)
    print(cabecalho)

    #for index, coluna in enumerate(cabecalho): #Enumere o cabeçalho
    #    print(index, coluna)

    dates, highs = [], []

    for linha in ler:
        data = datetime.strptime(linha[0], "%Y-%m-%d")
        dates.append(data)
        highs.append(int(linha[1]))

    print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', marker="o")

#Formata o gráfico
plt.title("Dias com alta temperatura, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

############################################################################################################

print("\n")

filename = "ehmatthes-pcc-v1.0.0-12-gf555082/sitka_weather_2014.csv"

with open(filename, "r") as file:
    ler = csv.reader(file)
    cabecalho = next(ler)
    print(cabecalho)

    dates, highs, lows = [], [], []

    for x in ler:
        data = datetime.strptime(x[0], "%Y-%m-%d")
        dates.append(data)

        high = int(x[1])
        highs.append(high)

        low = int(x[3])
        lows.append(low)

fig = plt.figure(dpi=256, figsize=(10, 6))

#alpha faz ficar mais opaco
plt.plot(dates, highs, color="green", alpha=0.5)
plt.plot(dates, lows, color="blue", alpha=0.5)

#Seria o espaçamento entre os dois Y
#X, Y1, Y2, a cor entre eles, opacidade
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.grid()
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)

#plt.savefig("images/2plotHighsLows.png")
plt.show()

##########################################################################################################

filename = "ehmatthes-pcc-v1.0.0-12-gf555082/death_valley_2014.csv"

with open(filename, "r") as file:
    ler = csv.reader(file)
    cabecalho = next(ler)

    dates, highs, lows = [], [], []

    for x in ler:
        print(x)
        try:
            data = datetime.strptime(x[0], "%Y-%m-%d")
            high = int(x[1])
            low = int(x[3])
        except ValueError:
            print(data, "missing data")
        else:
            dates.append(data)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=256, figsize=(10, 6))
plt.title("daily high and low temperatures - 2014\nDeath Valley, CA")
plt.plot(dates, highs, color="red", alpha=0.5)
plt.plot(dates, lows, color="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
fig.autofmt_xdate()

plt.show()