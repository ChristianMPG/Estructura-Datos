#Calcular el factoraial de un numero dado

x=int(input("Inserte un número a calcular el factorial"))
fac=1
for i in range (1,x+1):
    fac *= i

print(f"El facotirial es: {fac}")

