print("Vamos a indicar los número impares entre dos números")
inicio = int(input("Indica el número inicio: "))
fin = int(input("Indica un número fin: "))
numero = inicio
lista=[]
for numero in range(inicio, fin):
    if numero % 2 != 0:
        lista.append(numero)

print(lista)