class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 50

c = Coche()
print (c.velocidad, c.cilindrada, c.color, c.ruedas, c.puertas)