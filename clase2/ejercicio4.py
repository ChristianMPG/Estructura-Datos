#Crear un arreglo con 10 números aleatorios, imprimir en pantalla el promedio de estos numeors
import random
suma = 0


for i in range(1,11):
    numero = random.randint(1,30)
    print (f"El número aleatorio #{i} es {numero}")
    suma +=numero

prom= (suma/10)

print(f"El promedio de los números es {prom}")

