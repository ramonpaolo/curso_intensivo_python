from make_car import Car

meu_carro = Car("audi", "a4", 2016)

print(meu_carro.get_descriptive_name())

meu_carro.odometer_reading = 23
meu_carro.read_odometer()